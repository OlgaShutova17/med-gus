---
title: System Design — MVP
---

Минимальная архитектура для запуска продукта. Один сервер, без микросервисов.

---

## Стек технологий

| Компонент | Технология |
|---|---|
| Backend API | FastAPI (Python) |
| Frontend | Next.js |
| База данных | PostgreSQL |
| Объектное хранилище | MinIO (S3-совместимое) |
| Кэш / сессии | Redis |
| OCR | Tesseract OCR |
| Деплой | Docker Compose |

---

## Инфраструктура

Один сервер, все компоненты в Docker Compose:

```
Internet
    │
Load Balancer (Nginx)
    │
    ├── Frontend (Next.js)
    │
    └── Backend API (FastAPI)
              │
              ├── Redis (кэш сессий, AI-ответов)
              │
              ├── PostgreSQL (основная БД)
              │
              └── MinIO (файлы анализов)
```

---

## Модули backend

```
Backend API
│
├── auth          — регистрация, JWT-аутентификация
├── users         — профиль пользователя
├── themes        — проблемы/тематики
├── hypotheses    — гипотезы причин
├── events        — события (универсальная сущность)
├── consultations — данные консультаций
├── analyses      — анализы и их показатели
├── research      — инструментальные исследования
├── treatment     — курсы лечения и препараты
├── resolutions   — резолюции событий
├── files         — загрузка документов
└── ai            — OCR, NLP, инсайты
```

---

## Поток добавления анализа

```
1. Пользователь загружает файл
         │
         ▼
POST /files/upload
         │
         ▼
MinIO (S3) — файл сохранён
         │
         ▼
Запускается AI pipeline
         │
         ▼
OCR (Tesseract) → текст
         │
         ▼
Med NLP (LLM) → параметры
{ "parameter": "Гемоглобин", "value": 140, "unit": "г/л", "ref": "120-160" }
         │
         ▼
Сохранение в PostgreSQL
         │
         ▼
AI Analysis Engine → insights
         │
         ▼
UI получает результат
```

---

## AI Analysis Engine (MVP)

После извлечения параметров:

```
проверка нормы (по reference_ranges)
+
контекст пользователя (пол, возраст)
+
история предыдущих анализов
= insights + recommendations
```

Пример вывода:
```
Ферритин ниже нормы.
Возможный дефицит железа.
Рекомендуется консультация терапевта или гематолога.
```

---

## Безопасность

```
HTTPS          — весь трафик
JWT            — access + refresh tokens
Row-level security — пользователь видит только свои данные
Data encryption — медицинские данные в покое
```

---

## Redis — что кэшируется

```
AI-ответы         — повторные запросы не идут в LLM
Сессии            — JWT refresh tokens
Частые запросы    — списки тематик, последние события
```

---

## Ограничения MVP

- Нет горизонтального масштабирования — один инстанс backend
- Нет очереди задач (Celery/Kafka) — AI pipeline синхронный
- OCR через Tesseract — точность ниже, чем AWS Textract
- Один сервер — нет отказоустойчивости

Переход к следующей стадии описан в `scaling-architecture.md`.
