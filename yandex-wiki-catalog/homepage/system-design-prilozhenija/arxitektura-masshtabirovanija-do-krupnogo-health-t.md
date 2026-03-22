---
title: Архитектура масштабирования до крупного health-tech
order: 1
---

## Стадия 1 — MVP

```
Frontend
Backend
Postgres
Object storage
AI service
```

1 сервер.

---

## Стадия 2 — Product Market Fit

Появляются сервисы:

```
API Gateway
Auth Service
Medical Data Service
AI Service
Notification Service
```

---

## Стадия 3 — Growth

Архитектура:

```
Microservices
Event-driven architecture
```

---

## Сервисы

```
user-service
theme-service
medical-data-service
analysis-service
treatment-service
ai-service
notification-service
search-service
```

---

## Event Bus

Используется:

```
Kafka
или
RabbitMQ
```

События:

```
analysis_uploaded
analysis_parsed
insight_generated
treatment_updated
```

---

## Data Layer

```
PostgreSQL (core data)
ClickHouse (analytics)
Vector DB (AI)
```

---

## AI Layer

```
RAG pipeline
knowledge graph
pattern detection
predictive models
```

---

## Health Data Platform

Фактически система превращается в:

```
personal health data platform
```

---

## Потенциальные интеграции

```
лаборатории
телемедицина
фитнес-трекеры
страховые
```

---

## Главный актив продукта

Самая ценная вещь:

```
health timeline dataset
```

История:

```
симптомы
анализы
диагнозы
лечение
результаты
```

---

## Почему это может стать большим продуктом

Большинство health-apps хранят:

```
данные
```

Но не понимают:

```
причины
```

Если система научится находить:

```
patterns
risk prediction
treatment effectiveness
```

это становится **медицинским AI-ассистентом**.