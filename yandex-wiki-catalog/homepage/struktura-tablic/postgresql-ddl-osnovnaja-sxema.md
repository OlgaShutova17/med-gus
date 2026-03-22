---
title: PostgreSQL DDL (основная схема)
order: 1
---

## USERS

```
create table users (
    id uuid primary key default gen_random_uuid(),
    email text unique not null,
    password_hash text not null,
    name text,
    birth_date date,
    sex text,
    created_at timestamp default now()
);
```

---

## THEMES (проблемы пользователя)

```
create table themes (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id),
    title text not null,
    description text,
    status text default 'active',
    created_at timestamp default now()
);
```

status:

```
active
resolved
archived
```

---

## SYMPTOMS

```
create table symptoms (
    id uuid primary key,
    name text,
    description text
);
```

---

## THEME\_SYMPTOMS

```
create table theme_symptoms (
    id uuid primary key default gen_random_uuid(),
    theme_id uuid references themes(id),
    symptom_id uuid references symptoms(id),
    severity int,
    created_at timestamp default now()
);
```

---

## HYPOTHESES

Это важнейшая сущность.

```
create table hypotheses (
    id uuid primary key default gen_random_uuid(),
    theme_id uuid references themes(id),
    title text,
    description text,
    status text default 'testing',
    created_at timestamp default now()
);
```

status:

```
testing
confirmed
rejected
```

---

## EVENTS (основа timeline)

```
create table events (
    id uuid primary key default gen_random_uuid(),
    theme_id uuid references themes(id),
    event_type text,
    title text,
    description text,
    event_date date,
    created_at timestamp default now()
);
```

Типы:

```
consultation
analysis
research
treatment
note
```

---

## EVENT\_HYPOTHESES

Связывает события и гипотезы.

```
create table event_hypotheses (
    id uuid primary key default gen_random_uuid(),
    event_id uuid references events(id),
    hypothesis_id uuid references hypotheses(id),
    impact text
);
```

impact:

```
supports
rejects
neutral
```

Это ключевая таблица.

---

## CONSULTATIONS

```
create table consultations (
    id uuid primary key default gen_random_uuid(),
    event_id uuid references events(id),
    doctor_specialization text,
    clinic text,
    diagnosis text,
    recommendations text
);
```

---

## ANALYSES

Тип анализа.

```
create table analyses (
    id uuid primary key,
    name text,
    category text
);
```

---

## ANALYSIS\_RESULTS

```
create table analysis_results (
    id uuid primary key default gen_random_uuid(),
    event_id uuid references events(id),
    analysis_id uuid references analyses(id),
    lab_name text,
    result_date date,
    source_file_id uuid
);
```

---

## MEDICAL PARAMETERS

```
create table medical_parameters (
    id uuid primary key,
    code text unique,
    name text,
    category text
);
```

---

## ANALYSIS\_VALUES

```
create table analysis_values (
    id uuid primary key default gen_random_uuid(),
    analysis_result_id uuid references analysis_results(id),
    parameter_id uuid references medical_parameters(id),
    value numeric,
    unit text,
    reference_min numeric,
    reference_max numeric,
    status text
);
```

status:

```
low
normal
high
```

---

## FILE STORAGE

```
create table files (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id),
    storage_url text,
    file_type text,
    created_at timestamp default now()
);
```

---

## AI INSIGHTS

```
create table ai_insights (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references users(id),
    theme_id uuid references themes(id),
    insight_type text,
    content text,
    created_at timestamp default now()
);
```

---

## AI RECOMMENDATIONS

```
create table ai_recommendations (
    id uuid primary key default gen_random_uuid(),
    insight_id uuid references ai_insights(id),
    recommendation_type text,
    content text,
    priority int
);
```