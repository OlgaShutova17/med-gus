---
title: API Endpoints (REST)
order: 1
---

Базовый путь:

```
/api/v1
```

---

## AUTH

### регистрация

```
POST /auth/register
```

body

```
email
password
name
```

---

### login

```
POST /auth/login
```

response

```
access_token
refresh_token
```

---

## USERS

### профиль

```
GET /users/me
```

---

### обновление профиля

```
PATCH /users/me
```

---

## THEMES

### список тематик

```
GET /themes
```

---

### создать тематику

```
POST /themes
```

body

```
title
description
```

---

### получить тематику

```
GET /themes/{theme_id}
```

---

### удалить тематику

```
DELETE /themes/{theme_id}
```

---

## HYPOTHESES

### список гипотез

```
GET /themes/{theme_id}/hypotheses
```

---

### создать гипотезу

```
POST /themes/{theme_id}/hypotheses
```

---

### изменить статус гипотезы

```
PATCH /hypotheses/{id}
```

---

## EVENTS

### список событий

```
GET /themes/{theme_id}/events
```

filters

```
type
date_from
date_to
```

---

### создать событие

```
POST /events
```

body

```
theme_id
hypothesis_id
type
title
event_date
notes
```

---

## CONSULTATIONS

```
POST /events/{event_id}/consultation
```

---

## ANALYSES

### добавить анализ

```
POST /events/{event_id}/analysis
```

---

### добавить показатель анализа

```
POST /analyses/{analysis_id}/results
```

body

```
parameter_name
value
unit
reference_min
reference_max
```

---

## ДИНАМИКА АНАЛИЗОВ

```
GET /analysis-results/dynamics
```

query

```
parameter_name
period
```

response

```
date
value
reference_min
reference_max
```

---

## RESEARCH

```
POST /events/{event_id}/research
```

---

## FILES

### загрузка файла

```
POST /files
```

multipart

---

## RESOLUTION

```
POST /events/{event_id}/resolution
```

body

```
result
comment
```

---

## TREATMENT COURSES

### создать курс

```
POST /hypotheses/{id}/courses
```

---

### добавить препарат

```
POST /courses/{id}/medications
```

---

## AI endpoints

### анализ результатов

```
POST /ai/analyze-analysis
```

---

### рекомендации врача

```
POST /ai/recommend-specialist
```

---

## 5. Архитектурная особенность

Главный endpoint для UI — **timeline**.

```
GET /themes/{id}/timeline
```

Ответ:

```
events
consultations
analyses
research
resolutions
files
```

UI строится **вокруг хронологической ленты**.