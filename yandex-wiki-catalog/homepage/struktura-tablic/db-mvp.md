---
title: Схема БД — MVP
---

Минимальная схема для запуска. Без каталога медицинских параметров и Knowledge Graph — они добавляются после MVP.

Названия параметров анализов хранятся текстом (`parameter_name TEXT`). После MVP они нормализуются через таблицу `medical_parameters` (см. `_index.md`).

---

## ER-диаграмма

```
User
 └── Themes
       ├── Symptoms (через theme_symptoms)
       ├── Hypotheses
       │     └── TreatmentCourses
       │               └── Medications
       └── Events
             ├── Consultation
             ├── Analysis
             │     └── AnalysisResults  ← параметр текстом
             ├── Research
             └── Other
                   └── Resolution (1:1)
                   └── Files (1:N)
```

---

## USERS

```sql
CREATE TABLE users (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email         TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    name          TEXT,
    gender        TEXT,
    birth_date    DATE,
    created_at    TIMESTAMP DEFAULT NOW()
);
```

---

## THEMES (проблемы)

```sql
CREATE TABLE themes (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     UUID REFERENCES users(id) ON DELETE CASCADE,
    title       TEXT NOT NULL,
    description TEXT,
    status      TEXT DEFAULT 'active',  -- active | resolved | archived
    created_at  TIMESTAMP DEFAULT NOW()
);
```

---

## SYMPTOMS

```sql
CREATE TABLE symptoms (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT NOT NULL,
    description TEXT
);

CREATE TABLE theme_symptoms (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id   UUID REFERENCES themes(id) ON DELETE CASCADE,
    symptom_id UUID REFERENCES symptoms(id),
    severity   INT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## HYPOTHESES

```sql
CREATE TABLE hypotheses (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id    UUID REFERENCES themes(id) ON DELETE CASCADE,
    title       TEXT NOT NULL,
    description TEXT,
    status      TEXT DEFAULT 'new',  -- new | testing | confirmed | rejected
    created_at  TIMESTAMP DEFAULT NOW()
);
```

---

## EVENTS

```sql
CREATE TABLE events (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id       UUID REFERENCES users(id) ON DELETE CASCADE,
    theme_id      UUID REFERENCES themes(id) ON DELETE CASCADE,
    hypothesis_id UUID REFERENCES hypotheses(id),
    type          TEXT NOT NULL,  -- consultation | analysis | research | other
    title         TEXT,
    notes         TEXT,
    event_date    DATE,
    created_at    TIMESTAMP DEFAULT NOW()
);
```

---

## EVENT_HYPOTHESES (влияние события на гипотезу)

```sql
CREATE TABLE event_hypotheses (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id      UUID REFERENCES events(id) ON DELETE CASCADE,
    hypothesis_id UUID REFERENCES hypotheses(id) ON DELETE CASCADE,
    impact        TEXT  -- supports | rejects | neutral
);
```

---

## CONSULTATIONS

```sql
CREATE TABLE consultations (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id          UUID REFERENCES events(id) ON DELETE CASCADE,
    clinic            TEXT,
    doctor_name       TEXT,
    anamnesis_life    TEXT,
    anamnesis_disease TEXT,
    disease_course    TEXT,
    diagnosis         TEXT,
    treatment         TEXT,
    recommendations   TEXT,
    follow_up_date    DATE
);
```

---

## ANALYSES

```sql
CREATE TABLE analyses (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id      UUID REFERENCES events(id) ON DELETE CASCADE,
    analysis_type TEXT,
    lab_name      TEXT,
    analysis_date DATE
);
```

---

## ANALYSIS_RESULTS (показатели — параметр текстом)

В MVP названия параметров хранятся как свободный текст. После MVP заменяется связкой через `medical_parameters`.

```sql
CREATE TABLE analysis_results (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    analysis_id   UUID REFERENCES analyses(id) ON DELETE CASCADE,
    parameter_name TEXT NOT NULL,
    value          NUMERIC,
    unit           TEXT,
    reference_min  NUMERIC,
    reference_max  NUMERIC
);
```

---

## RESEARCH

```sql
CREATE TABLE research (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id        UUID REFERENCES events(id) ON DELETE CASCADE,
    research_type   TEXT,
    result_text     TEXT,
    findings        TEXT,
    recommendations TEXT
);
```

---

## TREATMENT_COURSES

```sql
CREATE TABLE treatment_courses (
    id            UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    hypothesis_id UUID REFERENCES hypotheses(id) ON DELETE CASCADE,
    name          TEXT,
    doctor        TEXT,
    diagnosis     TEXT,
    start_date    DATE,
    end_date      DATE,
    result        TEXT
);
```

---

## MEDICATIONS

```sql
CREATE TABLE medications (
    id        UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    course_id UUID REFERENCES treatment_courses(id) ON DELETE CASCADE,
    name      TEXT,
    dosage    TEXT,
    frequency TEXT
);
```

---

## RESOLUTIONS

```sql
CREATE TABLE resolutions (
    id         UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id   UUID REFERENCES events(id) ON DELETE CASCADE,
    result     TEXT CHECK (result IN ('helped', 'not_helped')),
    comment    TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## FILES

```sql
CREATE TABLE files (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id     UUID REFERENCES users(id) ON DELETE CASCADE,
    event_id    UUID REFERENCES events(id) ON DELETE CASCADE,
    file_url    TEXT,
    file_type   TEXT,
    uploaded_at TIMESTAMP DEFAULT NOW()
);
```

---

## Индексы

```sql
CREATE INDEX idx_events_user   ON events(user_id);
CREATE INDEX idx_events_theme  ON events(theme_id);
CREATE INDEX idx_events_type   ON events(type);
CREATE INDEX idx_ar_param      ON analysis_results(parameter_name);
CREATE INDEX idx_ar_analysis   ON analysis_results(analysis_id);
```

---

## Что добавляется после MVP

| Таблица | Назначение |
|---|---|
| `user_profiles` | Рост, вес, группа крови, хронические болезни |
| `medical_parameters` | Нормализованный справочник параметров (LOINC) |
| `parameter_aliases` | Hb / HGB / Гемоглобин → HEMOGLOBIN |
| `parameter_units` | Коэффициенты конвертации единиц |
| `reference_ranges` | Нормы по полу и возрасту |
| `analysis_values` | Замена `analysis_results`: привязка к справочнику |
| `drugs` | Каталог препаратов |
| `ai_insights` / `ai_recommendations` | Хранение AI-выводов |
| `diseases`, `symptom_disease`, `analysis_disease`, `treatment_disease` | Knowledge Graph |

Полная схема описана в `_index.md`.
