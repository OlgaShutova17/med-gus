---
title: API Endpoints (REST)
---

Базовый путь: `/api/v1`

---

## AUTH

```
POST /auth/register      # email, password, name
POST /auth/login         # → access_token, refresh_token
POST /auth/logout
GET  /auth/me
```

---

## USERS

```
GET   /users/me
PATCH /users/me
```

---

## THEMES (проблемы)

```
GET    /themes
POST   /themes           # title, description
GET    /themes/{id}
PATCH  /themes/{id}
DELETE /themes/{id}
```

---

## SYMPTOMS

```
GET    /symptoms
POST   /themes/{id}/symptoms
DELETE /themes/{id}/symptoms/{symptom_id}
```

---

## HYPOTHESES

```
GET    /themes/{id}/hypotheses
POST   /themes/{id}/hypotheses
PATCH  /hypotheses/{id}          # изменение статуса
DELETE /hypotheses/{id}
```

---

## EVENTS

```
GET    /themes/{id}/events       # ?type=&date_from=&date_to=
POST   /themes/{id}/events       # theme_id, hypothesis_id, type, title, event_date, notes
GET    /events/{id}
PATCH  /events/{id}
DELETE /events/{id}
```

---

## CONSULTATIONS

```
POST  /events/{id}/consultation
GET   /consultations/{id}
PATCH /consultations/{id}
```

---

## RESEARCH

```
POST  /events/{id}/research
GET   /research/{id}
PATCH /research/{id}
```

---

## ANALYSES

```
GET   /analyses
GET   /analyses/{id}
POST  /events/{id}/analysis
```

---

## ANALYSIS RESULTS (показатели)

```
GET  /analysis-results/{id}
POST /events/{id}/analysis
```

---

## ANALYSIS VALUES (значения показателей)

```
POST   /analysis-results/{id}/values    # parameter_name, value, unit, reference_min, reference_max
PATCH  /analysis-values/{id}
DELETE /analysis-values/{id}
```

---

## ДИНАМИКА АНАЛИЗОВ

```
GET /analysis-results/dynamics    # ?parameter_name=&period=
```

Response:
```
date, value, reference_min, reference_max
```

---

## ANALYTICS / PARAMETERS

```
GET /parameters
GET /parameters/{id}
GET /users/{id}/parameters/{parameter_id}/history
```

---

## FILES

```
POST   /files/upload    # multipart
GET    /files/{id}
DELETE /files/{id}
```

---

## RESOLUTIONS

```
POST /events/{id}/resolution    # result: helped|not_helped, comment
```

---

## TREATMENT

```
GET   /themes/{id}/treatments
POST  /themes/{id}/treatments
PATCH /treatments/{id}
```

---

## MEDICATIONS

```
POST   /treatments/{id}/medications    # name, dosage, frequency
PATCH  /medications/{id}
DELETE /medications/{id}
```

---

## AI

```
POST /ai/parse-analysis              # OCR-разбор загруженного документа
GET  /themes/{id}/insights           # AI-инсайты по тематике
GET  /themes/{id}/recommendations    # рекомендации специалистов
POST /ai/chat                        # { message, theme_id, context }
```

---

## DASHBOARD

```
GET /dashboard    # → themes, recent_events, insights, alerts
```

---

## Архитектурная особенность

Главный endpoint для UI — **timeline**:

```
GET /themes/{id}/timeline
```

Response:
```
events, consultations, analyses, research, resolutions, files
```

UI строится вокруг хронологической ленты событий.
