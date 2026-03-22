---
title: Архитектура AI ядра
order: 1
---

Цель AI-ядра — превратить неструктурированные медицинские данные в **структурированные знания \+ рекомендации**.

## Общий AI pipeline

```
User Upload
     ↓
File Storage
     ↓
OCR
     ↓
Medical NLP
     ↓
Data Normalization
     ↓
Medical Knowledge Graph
     ↓
AI Reasoning
     ↓
Insights
```

---

## Основные компоненты AI

## 1. Document ingestion

Принимает:

```
PDF
фото анализов
сканы
```

Функции:

```
распознавание документа
определение типа анализа
извлечение таблиц
```

---

## 2. OCR Engine

Распознаёт текст.

Для MVP:

```
Tesseract
```

Для production:

```
AWS Textract
Google Vision
```

Результат:

```
raw_text
tables
layout
```

---

## 3. Medical NLP Parser

LLM извлекает параметры.

Пример входа:

```
Гемоглобин 140 г/л
Ферритин 12 мкг/л
```

Результат:

```
[
 {
   parameter: "hemoglobin",
   value: 140,
   unit: "g/L"
 },
 {
   parameter: "ferritin",
   value: 12,
   unit: "ug/L"
 }
]
```

---

## Normalization Engine

Самая важная часть.

Она:

```
приводит названия
приводит единицы
находит стандартный параметр
```

Пример:

```
Hb
Hemoglobin
Гемоглобин
```

↓

```
HEMOGLOBIN
```

---

## Medical Knowledge Graph

Граф связей.

```
symptom
analysis
disease
treatment
drug
```

Связи:

```
symptom → disease
analysis → disease
treatment → outcome
```

Пример:

```
низкий ферритин
↓
железодефицит
↓
лечение железом
```

---

## AI Reasoning Engine

Модуль делает:

```
risk scoring
pattern detection
recommendations
```

Он анализирует:

```
анализы
симптомы
историю
гипотезы
```

---

## Insight Generator

Формирует объяснение пользователю.

Пример:

```
Ваш ферритин ниже нормы.

Это может указывать на:
— дефицит железа
— хроническую кровопотерю
— нарушение всасывания

Рекомендуется консультация терапевта.
```

---

## AI Assistant

Чат-интерфейс.

Использует:

```
RAG
knowledge graph
историю пользователя
```

Пример запроса:

```
Почему у меня высокий холестерин?
```

AI учитывает:

```
возраст
историю
анализы
```

---

## Архитектура AI сервисов

```
AI Services
│
├── document_service
├── ocr_service
├── medical_parser
├── normalization_service
├── knowledge_graph_service
├── reasoning_engine
└── ai_assistant
```