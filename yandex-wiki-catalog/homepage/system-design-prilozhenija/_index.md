---
title: System Design — Полная архитектура
---

Целевая архитектура продукта. MVP-реализация описана в `system-design-mvp.md`.

---

## Общая архитектура

Модульный монолит + выделенный AI-сервис:

```
                   CLIENTS
           ┌─────────────────────┐
           │  Web App (Next.js)  │
           │  Telegram Bot       │
           └──────────┬──────────┘
                      │ HTTPS
                      ▼
                API Gateway
                      │
            ┌─────────┴──────────┐
            │                    │
         Backend API          AI Service
      (Business Logic)       (AI Pipeline)
            │                    │
     ┌──────┤              ┌─────┤
     │      │              │     │
 PostgreSQL Redis       Vector DB  Object Storage
                          (pgvector/  (MinIO/S3)
                          Weaviate)
```

---

## Backend — слои

```
API Layer          REST endpoints, аутентификация, валидация, DTO
Application Layer  Бизнес-логика (services)
Domain Layer       Сущности, enums, value objects
Infrastructure     Репозитории, S3 storage, LLM client, PostgreSQL
```

### Модули

| Модуль | Ответственность | Сервисы |
|---|---|---|
| User | Авторизация, профиль, consent | auth_service, user_service |
| Problem (Themes) | Ядро продукта: проблемы и симптомы | theme_service, symptom_service |
| Hypothesis | Гипотезы, статусы, связь с событиями | hypothesis_service |
| Event | Центральная сущность: консультации, анализы, исследования | event_service, consultation_service, analysis_service, research_service |
| Treatment | Курсы лечения, препараты, трекинг | treatment_service, medication_service |
| AI | OCR, NLP, интерпретация, инсайты | ocr_service, medical_nlp_service, analysis_interpreter, recommendation_engine, insight_generator |
| Notification | Push, email, Telegram | notification_service |

---

## AI Service — пайплайн

```
User Upload (PDF/Фото)
      │
      ▼
File Storage (MinIO/S3)
      │
      ▼
Document Ingestion
      │
      ▼
OCR Engine
(MVP: Tesseract | Prod: AWS Textract / Google Vision)
      │
      ▼
Medical NLP Parser (LLM)
→ параметр, значение, единицы, референсы
      │
      ▼
Normalization Engine
(Hb / HGB / Гемоглобин → HEMOGLOBIN)
      │
      ▼
Medical Knowledge Graph
      │
      ▼
AI Reasoning Engine
→ risk score, pattern detection, hypothesis scoring
      │
      ▼
Insight Generator
→ patient-friendly recommendations
```

---

## Medical Knowledge Graph

Граф медицинских знаний — основа AI-рассуждений.

### Сущности

```
Symptom → Disease → Treatment → Drug
Parameter → Disease
```

### Пример фрагмента

```
усталость, головокружение, слабость
         │
         ▼
железодефицитная анемия
         │
         ▼
ферритин ↓, гемоглобин ↓
         │
         ▼
препараты железа
```

### Алгоритм вычисления вероятности гипотезы

```
score = symptom_weight × 0.3
      + analysis_weight × 0.5
      + history_weight × 0.2
```

Пример результата:
```
Дефицит железа  72%
Гипотиреоз      15%
Депрессия       13%
```

---

## Vector Database

Используется для RAG (Retrieval-Augmented Generation):

- Медицинские статьи и клинические рекомендации
- История пользователя для персонализации
- Справочник LOINC / SNOMED / ICD-10

Технологии: `pgvector` (MVP) → `Weaviate` / `Pinecone` (Production)

---

## AI Assistant

Чат-интерфейс использует RAG + Knowledge Graph:

```
Вопрос пользователя
       │
       ▼
Vector DB (релевантный контекст)
       │
       ▼
Knowledge Graph (медицинские связи)
       │
       ▼
LLM (генерация ответа)
       │
       ▼
Ответ с объяснением и источниками
```

---

## Data Flow — полный путь

```
User → Upload analysis
     → Backend → MinIO
     → AI pipeline → PostgreSQL
     → AI Insight → UI Timeline
```

---

## Notification Service

Каналы: Push, Telegram, Email

Триггеры:
- Напоминание о повторном анализе
- Следующий приём препарата (курс лечения)
- AI обнаружил критическое отклонение

---

## Главный актив продукта

```
Health Timeline Dataset
симптомы → анализы → диагнозы → лечение → результаты
```

Большинство health-apps хранят данные, но не понимают причины. Эта система строит **медицинское расследование** — связывает данные в контекст и ищет паттерны.
