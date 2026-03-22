---
title: Схема БД — Целевая (полная)
---

MVP-схема (без каталога параметров и Knowledge Graph) описана в `db-mvp.md`.

---

## ER-диаграмма

```
User ──────────────────────────────────────────────────┐
 └── UserProfile (1:1)                                  │
 └── Themes (1:N)                                       │
       ├── ThemeSymptoms → Symptoms                     │
       ├── Hypotheses (1:N)                             │
       │     └── TreatmentCourses (1:N)                 │
       │               └── Medications → Drugs          │
       └── Events (1:N) ──────────────────────────────┐ │
             ├── Consultation                          │ │
             ├── AnalysisResult → AnalysisValues       │ │
             │     └── MedicalParameter                │ │
             │           ├── ParameterAliases          │ │
             │           ├── ParameterUnits            │ │
             │           └── ReferenceRanges           │ │
             ├── Research                              │ │
             ├── EventHypotheses → Hypotheses          │ │
             ├── Resolution (1:1)                      │ │
             └── Files (через FileLinks) ──────────────┘ │
                   └────────────────────────────────────┘

Knowledge Graph:
  Diseases ←── SymptomDisease ── Symptoms
  Diseases ←── AnalysisDisease ── MedicalParameters
  Diseases ←── TreatmentDisease ── Treatments

AI:
  AIInsights → AIRecommendations
```

---

## USERS

```sql
CREATE TABLE users (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email       TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    name        TEXT,
    gender      TEXT,
    birth_date  DATE,
    created_at  TIMESTAMP DEFAULT NOW()
);
```

---

## THEMES (проблемы пользователя)

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

Связь: `user 1:N themes`

---

## SYMPTOMS

```sql
CREATE TABLE symptoms (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT,
    description TEXT
);

CREATE TABLE theme_symptoms (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    theme_id    UUID REFERENCES themes(id) ON DELETE CASCADE,
    symptom_id  UUID REFERENCES symptoms(id),
    severity    INT,
    created_at  TIMESTAMP DEFAULT NOW()
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

## EVENTS (основа timeline)

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

## EVENT_HYPOTHESES (связь событий и гипотез)

Ключевая таблица — хранит влияние события на гипотезу.

```sql
CREATE TABLE event_hypotheses (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id       UUID REFERENCES events(id) ON DELETE CASCADE,
    hypothesis_id  UUID REFERENCES hypotheses(id) ON DELETE CASCADE,
    impact         TEXT  -- supports | rejects | neutral
);
```

---

## CONSULTATIONS

```sql
CREATE TABLE consultations (
    id                 UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    event_id           UUID REFERENCES events(id) ON DELETE CASCADE,
    clinic             TEXT,
    doctor_name        TEXT,
    anamnesis_life     TEXT,
    anamnesis_disease  TEXT,
    disease_course     TEXT,
    diagnosis          TEXT,
    treatment          TEXT,
    recommendations    TEXT,
    follow_up_date     DATE
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

## MEDICAL_PARAMETERS (справочник параметров)

```sql
CREATE TABLE medical_parameters (
    id       UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    code     TEXT UNIQUE,
    name     TEXT,
    category TEXT
);
```

---

## ANALYSIS_RESULTS (показатели анализа)

```sql
CREATE TABLE analysis_results (
    id             UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    analysis_id    UUID REFERENCES analyses(id) ON DELETE CASCADE,
    parameter_name TEXT NOT NULL,
    value          NUMERIC,
    unit           TEXT,
    reference_min  NUMERIC,
    reference_max  NUMERIC
);
```

---

## ANALYSIS_VALUES (значения с привязкой к справочнику)

```sql
CREATE TABLE analysis_values (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    analysis_result_id UUID REFERENCES analysis_results(id),
    parameter_id      UUID REFERENCES medical_parameters(id),
    value             NUMERIC,
    unit              TEXT,
    reference_min     NUMERIC,
    reference_max     NUMERIC,
    status            TEXT  -- low | normal | high
);
```

---

## RESEARCH (МРТ / КТ / УЗИ)

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

## AI_INSIGHTS

```sql
CREATE TABLE ai_insights (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id      UUID REFERENCES users(id),
    theme_id     UUID REFERENCES themes(id),
    insight_type TEXT,
    content      TEXT,
    created_at   TIMESTAMP DEFAULT NOW()
);
```

---

## AI_RECOMMENDATIONS

```sql
CREATE TABLE ai_recommendations (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    insight_id          UUID REFERENCES ai_insights(id),
    recommendation_type TEXT,
    content             TEXT,
    priority            INT
);
```

---

## USER_PROFILES (расширенный профиль)

```sql
CREATE TABLE user_profiles (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id             UUID REFERENCES users(id) ON DELETE CASCADE,
    height              NUMERIC,
    weight              NUMERIC,
    blood_type          TEXT,
    chronic_conditions  TEXT,
    allergies           TEXT
);
```

---

## PARAMETER_ALIASES (нормализация названий)

Позволяет сопоставлять Hb / HGB / Гемоглобин → HEMOGLOBIN.

```sql
CREATE TABLE parameter_aliases (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parameter_id UUID REFERENCES medical_parameters(id) ON DELETE CASCADE,
    alias        TEXT NOT NULL,
    language     TEXT  -- ru, en, latin
);
```

---

## PARAMETER_UNITS (единицы измерения)

```sql
CREATE TABLE parameter_units (
    id                UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parameter_id      UUID REFERENCES medical_parameters(id),
    unit              TEXT NOT NULL,
    conversion_factor NUMERIC  -- для перевода в базовую единицу
);
```

---

## REFERENCE_RANGES (нормы по полу и возрасту)

```sql
CREATE TABLE reference_ranges (
    id           UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    parameter_id UUID REFERENCES medical_parameters(id),
    sex          TEXT,     -- male | female | any
    age_min      INT,
    age_max      INT,
    min_value    NUMERIC NOT NULL,
    max_value    NUMERIC NOT NULL,
    unit         TEXT
);
```

---

## DRUGS (каталог препаратов)

```sql
CREATE TABLE drugs (
    id               UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name             TEXT NOT NULL,
    active_substance TEXT
);
```

---

## FILE_LINKS (полиморфная привязка файлов)

Заменяет прямой `event_id` в `files` — позволяет привязывать файл к любой сущности.

```sql
CREATE TABLE file_links (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    file_id     UUID REFERENCES files(id) ON DELETE CASCADE,
    entity_type TEXT NOT NULL,  -- event | consultation | research | analysis
    entity_id   UUID NOT NULL
);
```

---

## KNOWLEDGE GRAPH

Основа AI-рассуждений: связи симптомов, параметров и заболеваний.

```sql
CREATE TABLE diseases (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name        TEXT NOT NULL,
    icd_code    TEXT,
    description TEXT
);

-- вес связи symptom → disease
CREATE TABLE symptom_disease (
    symptom_id UUID REFERENCES symptoms(id),
    disease_id UUID REFERENCES diseases(id),
    weight     NUMERIC,
    PRIMARY KEY (symptom_id, disease_id)
);

-- вес связи analysis_parameter → disease
CREATE TABLE analysis_disease (
    parameter_id UUID REFERENCES medical_parameters(id),
    disease_id   UUID REFERENCES diseases(id),
    weight       NUMERIC,
    PRIMARY KEY (parameter_id, disease_id)
);

-- эффективность лечения при заболевании
CREATE TABLE treatment_disease (
    treatment_id  UUID REFERENCES treatment_courses(id),
    disease_id    UUID REFERENCES diseases(id),
    effectiveness NUMERIC,
    PRIMARY KEY (treatment_id, disease_id)
);
```

---

## Индексы

```sql
CREATE INDEX idx_events_user   ON events(user_id);
CREATE INDEX idx_events_theme  ON events(theme_id);
CREATE INDEX idx_events_type   ON events(type);

CREATE INDEX idx_analysis_results_param    ON analysis_results(parameter_name);
CREATE INDEX idx_analysis_results_analysis ON analysis_results(analysis_id);

CREATE INDEX idx_param_aliases  ON parameter_aliases(alias);
CREATE INDEX idx_ref_ranges     ON reference_ranges(parameter_id, sex);
CREATE INDEX idx_file_links     ON file_links(entity_type, entity_id);
```
