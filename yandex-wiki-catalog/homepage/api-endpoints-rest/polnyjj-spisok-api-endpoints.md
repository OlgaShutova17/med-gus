---
title: Полный список API endpoints
order: 1
---

Все API построены как:

```
/api/v1/
```

---

## AUTH

```
POST /auth/register
POST /auth/login
POST /auth/logout
GET  /auth/me
```

---

## USERS

```
GET /users/profile
PATCH /users/profile
```

---

## THEMES (Проблемы)

```
GET /themes
POST /themes
GET /themes/{id}
PATCH /themes/{id}
DELETE /themes/{id}
```

---

## SYMPTOMS

```
GET /symptoms
POST /themes/{id}/symptoms
DELETE /themes/{id}/symptoms/{symptom_id}
```

---

## HYPOTHESES

```
GET /themes/{id}/hypotheses
POST /themes/{id}/hypotheses
PATCH /hypotheses/{id}
DELETE /hypotheses/{id}
```

---

## EVENTS

```
GET /themes/{id}/events
POST /themes/{id}/events
GET /events/{id}
PATCH /events/{id}
DELETE /events/{id}
```

---

## CONSULTATIONS

```
POST /events/{id}/consultation
GET /consultations/{id}
PATCH /consultations/{id}
```

---

## RESEARCH

```
POST /events/{id}/research
GET /research/{id}
PATCH /research/{id}
```

---

## ANALYSES

```
GET /analyses
GET /analyses/{id}
```

---

## ANALYSIS RESULTS

```
POST /events/{id}/analysis
GET /analysis-results/{id}
```

---

## ANALYSIS VALUES

```
POST /analysis-results/{id}/values
PATCH /analysis-values/{id}
DELETE /analysis-values/{id}
```

---

## ANALYTICS

```
GET /parameters
GET /parameters/{id}

GET /users/{id}/parameters/{parameter_id}/history
```

---

## FILES

```
POST /files/upload
GET /files/{id}
DELETE /files/{id}
```

---

## AI

### OCR

```
POST /ai/parse-analysis
```

---

### AI insights

```
GET /themes/{id}/insights
```

---

### AI recommendations

```
GET /themes/{id}/recommendations
```

---

### AI assistant

```
POST /ai/chat
```

body:

```
message
theme_id
context
```

---

## TREATMENT

```
GET /themes/{id}/treatments
POST /themes/{id}/treatments
PATCH /treatments/{id}
```

---

## MEDICATIONS

```
POST /treatments/{id}/medications
PATCH /medications/{id}
DELETE /medications/{id}
```

---

## DASHBOARD

```
GET /dashboard
```

Ответ:

```
themes
recent_events
insights
alerts
```