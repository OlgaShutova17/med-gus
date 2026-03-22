---
title: System Design приложения
order: 1
---

## Общая архитектура

Лучший вариант — **модульный монолит \+ AI сервис**.

```
                   CLIENTS
           ┌─────────────────────┐
           │ Web App (Next.js)   │
           │ Telegram Bot        │
           └──────────┬──────────┘
                      │
                      │ HTTPS
                      │
                API Gateway
                      │
            ┌─────────┴──────────┐
            │                     │
         Backend API         AI Service
      (Business Logic)     (AI Pipeline)
            │                     │
            │                     │
      PostgreSQL DB         Vector DB
            │                     │
            │
      Object Storage
       (S3 / MinIO)
```

---

## Backend сервис

Основной сервер:

```
Backend API
```

Содержит:

```
Auth module
User module
Theme module
Event module
Analysis module
Research module
Treatment module
Resolution module
File module
AI module
```

---

## Поток добавления анализа

### 1. пользователь загружает файл

```
POST /files/upload
```

↓

файл сохраняется

```
S3 / MinIO
```

↓

запускается AI pipeline.

---

### 2. AI обработка

```
file
 ↓
OCR
 ↓
text
 ↓
Med NLP
 ↓
parameters extraction
 ↓
save results
```

---

## OCR сервис

Для MVP:

```
Tesseract OCR
```

или

```
AWS Textract
```

Результат:

```
текст анализа
```

---

## Med NLP сервис

LLM извлекает:

```
параметр
значение
единицы
референсы
```

Пример:

```
Гемоглобин — 140 г/л
Референс: 120–160
```

---

## AI Analysis Engine

После сохранения данных система делает анализ.

Алгоритм:

```
проверка нормы
+
контекст пользователя
+
история анализов
```

Результат:

```
insights
recommendations
```

Пример:

```
Ферритин ниже нормы.
Возможный дефицит железа.
Рекомендуется терапевт или гематолог.
```

---

## AI Knowledge Layer

Для будущего масштабирования.

```
symptoms
analyses
diagnoses
treatments
```

Связи:

```
symptom → disease
analysis → disease
treatment → outcome
```

---

## Vector Database (для AI)

Используется для:

```
RAG (retrieval augmented generation)
```

Примеры данных:

```
медицинские статьи
клинические рекомендации
история пользователей
```

Технологии:

```
pgvector
Weaviate
Pinecone
```

---

## Notification сервис

Отправляет:

```
push
telegram
email
```

События:

```
повторный анализ
напоминание о лечении
```

---

## Data Flow

Пример полного процесса:

```
User
 ↓
Upload analysis
 ↓
Backend
 ↓
Storage
 ↓
AI pipeline
 ↓
PostgreSQL
 ↓
AI Insight
 ↓
UI
```

---

## Деплой архитектура

Для MVP достаточно:

```
Docker
+
1 сервер
```

Стек:

```
Backend (FastAPI)
Frontend (Next.js)
PostgreSQL
MinIO
Redis
```

---

## Архитектура инфраструктуры

```
                Internet
                    │
               Load Balancer
                    │
           ┌────────┴────────┐
           │                 │
        Frontend         Backend
         (Next.js)        API
                              │
                         Redis cache
                              │
                         PostgreSQL
                              │
                          MinIO
```

---

## Масштабирование

Когда появится много пользователей:

```
Backend
↓
Microservices
```

Разделение:

```
AI service
Notification service
Medical data service
```

---

## Кеширование

Redis используется для:

```
AI responses
user sessions
frequent queries
```

---

## Безопасность медицинских данных

Обязательно:

```
HTTPS
JWT auth
row-level security
data encryption
```