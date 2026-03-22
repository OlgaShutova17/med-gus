---
title: Деплой MVP на Selectel
---

Инструкция по развёртыванию первой рабочей версии: PostgreSQL с MVP-схемой, FastAPI backend (регистрация, авторизация, создание и список тематик), Next.js frontend (главная + форма создания тематики).

---

## 1. Сервер в Selectel

1. Войди в [Selectel Cloud](https://selectel.ru/services/cloud/servers/)
2. Создай сервер:
   - **ОС:** Ubuntu 22.04 LTS
   - **Конфигурация:** 2 vCPU / 4 GB RAM / 40 GB SSD
   - **Сеть:** публичный IP включить
3. Подключись по SSH:

```bash
ssh root@<IP_СЕРВЕРА>
```

---

## 2. Установка Docker

```bash
apt update && apt install -y docker.io docker-compose-plugin
systemctl enable docker && systemctl start docker
```

---

## 3. Структура проекта на сервере

```bash
mkdir -p /app && cd /app
```

```
/app
├── docker-compose.yml
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── requirements.txt
│   └── init.sql
└── frontend/
    ├── Dockerfile
    ├── next.config.js
    ├── package.json
    └── src/app/
        ├── page.tsx
        └── themes/new/page.tsx
```

---

## 4. База данных — init.sql

Файл `/app/backend/init.sql` — выполняется автоматически при первом старте контейнера PostgreSQL.

```sql
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

CREATE TABLE users (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email         TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    name          TEXT,
    created_at    TIMESTAMP DEFAULT NOW()
);

CREATE TABLE themes (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     UUID REFERENCES users(id) ON DELETE CASCADE,
    title       TEXT NOT NULL,
    description TEXT,
    status      TEXT DEFAULT 'active',
    created_at  TIMESTAMP DEFAULT NOW()
);

CREATE INDEX idx_themes_user ON themes(user_id);
```

Полная MVP-схема (все таблицы) — в `../struktura-tablic/db-mvp.md`.

---

## 5. Backend (FastAPI)

### requirements.txt

```
fastapi==0.111.0
uvicorn==0.29.0
asyncpg==0.29.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0
pydantic==2.7.0
```

### main.py

```python
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jose import jwt, JWTError
from passlib.context import CryptContext
import asyncpg, os, uuid
from datetime import datetime, timedelta

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY   = os.getenv("SECRET_KEY", "change-me-in-production")
ALGORITHM    = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24

app = FastAPI(title="МедДневник API")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

pwd_ctx = CryptContext(schemes=["bcrypt"])
oauth2  = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")

# --- DB ---

async def get_db():
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()

# --- Auth helpers ---

def make_token(user_id: str) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    return jwt.encode({"sub": user_id, "exp": expire}, SECRET_KEY, ALGORITHM)

async def current_user(token: str = Depends(oauth2), db=Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    row = await db.fetchrow("SELECT id FROM users WHERE id=$1", uuid.UUID(user_id))
    if not row:
        raise HTTPException(status_code=401, detail="User not found")
    return str(row["id"])

# --- Schemas ---

class RegisterIn(BaseModel):
    email: str
    password: str
    name: str | None = None

class ThemeIn(BaseModel):
    title: str
    description: str | None = None

# --- Auth ---

@app.post("/api/v1/auth/register")
async def register(body: RegisterIn, db=Depends(get_db)):
    existing = await db.fetchrow("SELECT id FROM users WHERE email=$1", body.email)
    if existing:
        raise HTTPException(400, "Email already registered")
    uid = await db.fetchval(
        "INSERT INTO users(email, password_hash, name) VALUES($1,$2,$3) RETURNING id",
        body.email, pwd_ctx.hash(body.password), body.name
    )
    return {"access_token": make_token(str(uid))}

@app.post("/api/v1/auth/login")
async def login(form: OAuth2PasswordRequestForm = Depends(), db=Depends(get_db)):
    row = await db.fetchrow("SELECT id, password_hash FROM users WHERE email=$1", form.username)
    if not row or not pwd_ctx.verify(form.password, row["password_hash"]):
        raise HTTPException(401, "Wrong email or password")
    return {"access_token": make_token(str(row["id"])), "token_type": "bearer"}

# --- Themes ---

@app.get("/api/v1/themes")
async def list_themes(user_id: str = Depends(current_user), db=Depends(get_db)):
    rows = await db.fetch(
        "SELECT id, title, description, status, created_at FROM themes "
        "WHERE user_id=$1 ORDER BY created_at DESC",
        uuid.UUID(user_id)
    )
    return [dict(r) for r in rows]

@app.post("/api/v1/themes", status_code=201)
async def create_theme(body: ThemeIn, user_id: str = Depends(current_user), db=Depends(get_db)):
    if not body.title.strip():
        raise HTTPException(422, "Введите название тематики")
    row = await db.fetchrow(
        "INSERT INTO themes(user_id, title, description) VALUES($1,$2,$3) "
        "RETURNING id, title, status, created_at",
        uuid.UUID(user_id), body.title.strip(), body.description
    )
    return dict(row)
```

### Dockerfile

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

## 6. Frontend (Next.js)

### next.config.js

```js
/** @type {import('next').NextConfig} */
module.exports = { output: 'standalone' }
```

### package.json

```json
{
  "name": "meddnevnik",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "14.2.3",
    "react": "^18",
    "react-dom": "^18"
  },
  "devDependencies": {
    "@types/node": "^20",
    "@types/react": "^18",
    "typescript": "^5"
  }
}
```

### src/app/page.tsx — главная (список тематик)

```tsx
'use client'
import { useEffect, useState } from 'react'
import Link from 'next/link'

const API = process.env.NEXT_PUBLIC_API_URL

type Theme = {
  id: string
  title: string
  description: string
  status: string
  created_at: string
}

export default function Home() {
  const [themes, setThemes] = useState<Theme[]>([])
  const token = typeof window !== 'undefined' ? localStorage.getItem('token') : null

  useEffect(() => {
    if (!token) return
    fetch(`${API}/api/v1/themes`, {
      headers: { Authorization: `Bearer ${token}` }
    })
      .then(r => r.json())
      .then(setThemes)
  }, [token])

  if (!token) return (
    <main style={{ padding: 32 }}>
      <h1>МедДневник</h1>
      <p>Войдите, чтобы видеть тематики.</p>
      <Link href="/login">Войти</Link>
    </main>
  )

  return (
    <main style={{ padding: 32 }}>
      <h1>Мои тематики</h1>
      <Link href="/themes/new">+ Создать тематику</Link>
      <ul style={{ marginTop: 24 }}>
        {themes.map(t => (
          <li key={t.id} style={{ marginBottom: 12 }}>
            <strong>{t.title}</strong>
            {t.description && <span> — {t.description}</span>}
            <br />
            <small>{new Date(t.created_at).toLocaleDateString('ru-RU')}</small>
          </li>
        ))}
        {themes.length === 0 && <li>Тематик пока нет.</li>}
      </ul>
    </main>
  )
}
```

### src/app/themes/new/page.tsx — форма создания тематики

```tsx
'use client'
import { useState } from 'react'
import { useRouter } from 'next/navigation'

const API = process.env.NEXT_PUBLIC_API_URL

export default function NewTheme() {
  const router = useRouter()
  const [title, setTitle]      = useState('')
  const [description, setDesc] = useState('')
  const [error, setError]      = useState('')

  async function submit(e: React.FormEvent) {
    e.preventDefault()
    if (!title.trim()) { setError('Введите название тематики'); return }
    const token = localStorage.getItem('token')
    const res = await fetch(`${API}/api/v1/themes`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${token}`
      },
      body: JSON.stringify({ title, description })
    })
    if (res.ok) {
      router.push('/')
    } else {
      const d = await res.json()
      setError(d.detail || 'Ошибка сервера')
    }
  }

  return (
    <main style={{ padding: 32 }}>
      <h1>Новая тематика</h1>
      <form onSubmit={submit} style={{ display: 'flex', flexDirection: 'column', gap: 12, maxWidth: 400 }}>
        <input
          placeholder="Название тематики *"
          value={title}
          onChange={e => setTitle(e.target.value)}
          style={{ padding: 8, fontSize: 16 }}
        />
        <textarea
          placeholder="Описание (необязательно)"
          value={description}
          onChange={e => setDesc(e.target.value)}
          rows={3}
          style={{ padding: 8, fontSize: 16 }}
        />
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <button type="submit" style={{ padding: '10px 24px' }}>Создать</button>
      </form>
    </main>
  )
}
```

### Dockerfile

```dockerfile
FROM node:20-alpine AS builder
WORKDIR /app
COPY package.json package-lock.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
COPY --from=builder /app/public ./public
ENV NEXT_TELEMETRY_DISABLED=1
CMD ["node", "server.js"]
```

---

## 7. Docker Compose

Файл `/app/docker-compose.yml`:

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_DB: meddnevnik
      POSTGRES_USER: med
      POSTGRES_PASSWORD: strongpassword123
    volumes:
      - pgdata:/var/lib/postgresql/data
      - ./backend/init.sql:/docker-entrypoint-initdb.d/init.sql
    restart: always

  backend:
    build: ./backend
    environment:
      DATABASE_URL: postgresql://med:strongpassword123@postgres:5432/meddnevnik
      SECRET_KEY: замени-на-случайную-строку-64-символа
    ports:
      - "8000:8000"
    depends_on:
      - postgres
    restart: always

  frontend:
    build: ./frontend
    environment:
      NEXT_PUBLIC_API_URL: http://<IP_СЕРВЕРА>:8000
    ports:
      - "3000:3000"
    depends_on:
      - backend
    restart: always

volumes:
  pgdata:
```

> Замени `strongpassword123` и `SECRET_KEY` на случайные значения перед деплоем.

---

## 8. Запуск

```bash
cd /app
docker compose up --build -d
```

Проверка логов:

```bash
docker compose logs -f backend
docker compose logs -f frontend
```

---

## 9. Проверка через curl

```bash
# Регистрация
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@mail.ru","password":"pass123","name":"Тест"}'

# Ответ: {"access_token": "eyJ..."}

# Создание тематики
curl -X POST http://localhost:8000/api/v1/themes \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <TOKEN>" \
  -d '{"title":"Мигрени","description":"Головные боли с 2024 года"}'

# Список тематик
curl http://localhost:8000/api/v1/themes \
  -H "Authorization: Bearer <TOKEN>"
```

Swagger UI доступен на `http://<IP>:8000/docs`

---

## 10. Открыть порты в Selectel

В панели Selectel → **Сети → Firewall**, добавить правила:

| Порт | Назначение |
|---|---|
| 22 | SSH |
| 3000 | Frontend |
| 8000 | Backend API |

Или через UFW на сервере:

```bash
ufw allow 22 && ufw allow 3000 && ufw allow 8000 && ufw enable
```

---

## Итог

| Компонент | Адрес |
|---|---|
| Frontend | `http://<IP>:3000` |
| Backend API | `http://<IP>:8000` |
| Swagger UI | `http://<IP>:8000/docs` |
| PostgreSQL | внутри Docker (наружу не открыт) |

Следующий шаг — добавить Nginx как reverse proxy, настроить домен и HTTPS (Let's Encrypt).
