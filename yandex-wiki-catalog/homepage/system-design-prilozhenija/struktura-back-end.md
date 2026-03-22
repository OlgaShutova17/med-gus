---
title: Структура back-end
order: 1
---

## Общая архитектура backend

```
Backend
│
├── API Layer
│
├── Application Layer
│
├── Domain Layer
│
├── Infrastructure Layer
│
└── Integrations
```

---

## Архитектура слоев

## 1. API Layer

Отвечает за:

* REST endpoints

* аутентификацию

* валидацию

* DTO

```
api
 ├── auth
 │    └── auth_controller
 │
 ├── themes
 │    └── themes_controller
 │
 ├── events
 │    └── events_controller
 │
 ├── analyses
 │    └── analyses_controller
 │
 ├── consultations
 │
 ├── research
 │
 ├── hypothesis
 │
 ├── treatment
 │
 └── ai
```

---

## 2. Application Layer

Слой бизнес-логики.

```
services
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

Пример:

```
analysis_service

[tab:create_analysis::]
[/tab]
[tab:add_analysis_result::]
[/tab]
[tab:get_analysis_dynamics::]
[/tab]
[tab:parse_analysis_document::]
```

---

## 3. Domain Layer

Чистая бизнес-модель.

```
domain
 ├── entities
 │
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
 ├── enums
 │
 │   ├── event_type
 │   ├── hypothesis_status
 │   ├── resolution_type
 │
 └── value_objects
     ├── medical_parameter
     ├── reference_range
```

---

## 4. Infrastructure Layer

Работа с БД и внешними сервисами.

```
infrastructure
 ├── repositories
 │
 │   ├── user_repository
 │   ├── theme_repository
 │   ├── event_repository
 │   ├── analysis_repository
 │
 ├── storage
 │
 │   └── s3_storage
 │
 ├── ai
 │
 │   ├── llm_client
 │   ├── ocr_service
 │
 └── database
     └── postgres
```

---

## Backend modules

Лучше разделить backend на **6 основных модулей**.

---

## 1. User module

Отвечает за:

* авторизацию

* профиль

* consent на обработку мед данных

Сервисы:

```
auth_service
user_service
```

---

## 2. Problem module (Themes)

Ядро продукта.

```
theme_service
symptom_service
```

Функции:

* создать проблему

* добавить описание

* добавить симптомы

---

## 3. Hypothesis module

```
hypothesis_service
```

Функции:

* создание гипотез

* изменение статуса

* связь с событиями

---

## 4. Event module

События — центральная сущность.

```
event_service
consultation_service
analysis_service
research_service
```

Типы событий:

```
consultation
analysis
research
other
```

---

## 5. Treatment module

```
treatment_service
medication_service
```

Функции:

* создание курса лечения

* отслеживание выполнения

---

## 6. AI module

Самый интересный блок.

```
ai_module
```

Состоит из:

```
ocr_service
medical_nlp_service
analysis_interpreter
recommendation_engine
insight_generator
```

---

## AI pipeline

Когда пользователь загружает анализ:

```
file upload
      ↓
OCR
      ↓
LLM extraction
      ↓
entity normalization
      ↓
save to DB
      ↓
AI analysis
      ↓
insights
```

---

## Пример обработки анализа

```
PDF анализ
    ↓
OCR
    ↓
text
    ↓
LLM
    ↓
{
 "parameter": "Гемоглобин",
 "value": 140,
 "unit": "г/л",
 "ref": "120-160"
}
```

---

## AI Insight Engine

AI формирует:

```
summary
risk_level
recommendations
doctor_specialization
```

Пример ответа:

```
"Гемоглобин в норме.
Ферритин ниже нормы.
Рекомендуется консультация терапевта."
```

---

## Notification module

Будущая система:

```
notifications
 ├── push
 ├── email
 └── telegram
```

События:

```
повторный анализ
контроль лечения
```

---

## Дерево backend проекта

Пример структуры:

```
backend
│
├── api
│
├── services
│
├── domain
│
├── repositories
│
├── ai
│
├── storage
│
├── database
│
└── config
```[/tab]
