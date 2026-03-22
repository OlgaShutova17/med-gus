---
title: Структура backend (код)
---

Описание слоёв и модулей для разработчика. Технологический стек: FastAPI (Python).

---

## Слои

```
backend/
├── api/            ← REST endpoints, DTO, валидация
├── services/       ← бизнес-логика
├── domain/         ← сущности, enums, value objects
├── repositories/   ← работа с БД
├── ai/             ← OCR, NLP, reasoning
├── storage/        ← S3/MinIO клиент
├── database/       ← PostgreSQL конфигурация
└── config/         ← настройки приложения
```

---

## API Layer

REST-контроллеры, аутентификация, валидация входящих DTO.

```
api/
├── auth/
├── themes/
├── events/
├── analyses/
├── consultations/
├── research/
├── hypotheses/
├── treatment/
└── ai/
```

---

## Application Layer (Services)

```
services/
├── user_service
├── theme_service
├── hypothesis_service
├── event_service
├── consultation_service
├── analysis_service
├── research_service
├── treatment_service
├── resolution_service
├── file_service
└── ai_service
```

`analysis_service` отвечает за:
- create_analysis
- add_analysis_result
- get_analysis_dynamics
- parse_analysis_document

---

## Domain Layer

Чистые бизнес-объекты без зависимостей от БД.

```
domain/
├── entities/
│   ├── user
│   ├── theme
│   ├── hypothesis
│   ├── event
│   ├── analysis
│   ├── research
│   ├── consultation
│   ├── treatment_course
│   └── resolution
│
├── enums/
│   ├── event_type         # consultation | analysis | research | other
│   ├── hypothesis_status  # new | testing | confirmed | rejected
│   └── resolution_type    # helped | not_helped
│
└── value_objects/
    ├── medical_parameter
    └── reference_range
```

---

## Infrastructure Layer

```
infrastructure/
├── repositories/
│   ├── user_repository
│   ├── theme_repository
│   ├── event_repository
│   └── analysis_repository
│
├── storage/
│   └── s3_storage          # MinIO / S3 клиент
│
├── ai/
│   ├── llm_client          # OpenAI / локальная LLM
│   └── ocr_service         # Tesseract / AWS Textract
│
└── database/
    └── postgres             # SQLAlchemy / asyncpg
```

---

## AI Module

```
ai/
├── ocr_service             # PDF/фото → текст
├── medical_nlp_service     # текст → структурированные параметры
├── normalization_service   # Hb → HEMOGLOBIN
├── analysis_interpreter    # параметры → оценка отклонений
├── recommendation_engine   # отклонения → врач-специалист
└── insight_generator       # генерация текста для пользователя
```

### Пример AI-пайплайна

```python
# Входные данные — PDF анализа
pdf → ocr_service → raw_text
raw_text → medical_nlp_service → [
    {"parameter": "Гемоглобин", "value": 140, "unit": "г/л", "ref_min": 120, "ref_max": 160},
    {"parameter": "Ферритин",   "value": 10,  "unit": "мкг/л", "ref_min": 20, "ref_max": 150}
]
→ analysis_interpreter → {"status": "low", "deviation": -50%}
→ insight_generator → "Ферритин значительно ниже нормы. Рекомендуется консультация терапевта."
```

---

## Notification Module

```
notifications/
├── push_service
├── email_service
└── telegram_service
```

Триггеры: повторный анализ, контроль приёма препаратов.
