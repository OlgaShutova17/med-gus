---
title: Структура таблиц DDL
order: 1
---

## USERS

```
CREATE TABLE users (
    id UUID PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    name TEXT,
    gender TEXT,
    birth_date DATE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## THEMES (проблемы)

```
CREATE TABLE themes (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

Связь

```
user 1:N themes
```

---

## HYPOTHESES

```
CREATE TABLE hypotheses (
    id UUID PRIMARY KEY,
    theme_id UUID REFERENCES themes(id) ON DELETE CASCADE,
    title TEXT NOT NULL,
    description TEXT,
    status TEXT DEFAULT 'new',
    created_at TIMESTAMP DEFAULT NOW()
);
```

Статусы:

```
new
testing
confirmed
rejected
```

---

## EVENTS (универсальная таблица)

Типы событий из требований:

```
consultation
analysis
research
other
```

```
CREATE TABLE events (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    theme_id UUID REFERENCES themes(id) ON DELETE CASCADE,
    hypothesis_id UUID REFERENCES hypotheses(id),
    type TEXT NOT NULL,
    title TEXT,
    notes TEXT,
    event_date DATE,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## CONSULTATIONS

```
CREATE TABLE consultations (
    id UUID PRIMARY KEY,
    event_id UUID REFERENCES events(id) ON DELETE CASCADE,
    clinic TEXT,
    doctor_name TEXT,
    anamnesis_life TEXT,
    anamnesis_disease TEXT,
    disease_course TEXT,
    diagnosis TEXT,
    treatment TEXT,
    recommendations TEXT,
    follow_up_date DATE
);
```

---

## ANALYSES

```
CREATE TABLE analyses (
    id UUID PRIMARY KEY,
    event_id UUID REFERENCES events(id) ON DELETE CASCADE,
    analysis_type TEXT,
    lab_name TEXT,
    analysis_date DATE
);
```

---

## ANALYSIS\_RESULTS (показатели)

```
CREATE TABLE analysis_results (
    id UUID PRIMARY KEY,
    analysis_id UUID REFERENCES analyses(id) ON DELETE CASCADE,
    parameter_name TEXT NOT NULL,
    value NUMERIC,
    unit TEXT,
    reference_min NUMERIC,
    reference_max NUMERIC
);
```

---

## RESEARCH (МРТ / КТ / УЗИ)

```
CREATE TABLE research (
    id UUID PRIMARY KEY,
    event_id UUID REFERENCES events(id) ON DELETE CASCADE,
    research_type TEXT,
    result_text TEXT,
    findings TEXT,
    recommendations TEXT
);
```

---

## TREATMENT COURSES

```
CREATE TABLE treatment_courses (
    id UUID PRIMARY KEY,
    hypothesis_id UUID REFERENCES hypotheses(id) ON DELETE CASCADE,
    name TEXT,
    doctor TEXT,
    diagnosis TEXT,
    start_date DATE,
    end_date DATE,
    result TEXT
);
```

---

## MEDICATIONS

```
CREATE TABLE medications (
    id UUID PRIMARY KEY,
    course_id UUID REFERENCES treatment_courses(id) ON DELETE CASCADE,
    name TEXT,
    dosage TEXT,
    frequency TEXT
);
```

---

## RESOLUTIONS

```
CREATE TABLE resolutions (
    id UUID PRIMARY KEY,
    event_id UUID REFERENCES events(id) ON DELETE CASCADE,
    result TEXT CHECK (result IN ('helped','not_helped')),
    comment TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## FILES

```
CREATE TABLE files (
    id UUID PRIMARY KEY,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    event_id UUID REFERENCES events(id) ON DELETE CASCADE,
    file_url TEXT,
    file_type TEXT,
    uploaded_at TIMESTAMP DEFAULT NOW()
);
```

---

## SYMPTOMS

```
CREATE TABLE symptoms (
    id UUID PRIMARY KEY,
    theme_id UUID REFERENCES themes(id) ON DELETE CASCADE,
    name TEXT,
    description TEXT,
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## 3. Индексы (важно для производительности)

```
CREATE INDEX idx_events_user ON events(user_id);

CREATE INDEX idx_events_theme ON events(theme_id);

CREATE INDEX idx_events_type ON events(type);

CREATE INDEX idx_analysis_results_param
ON analysis_results(parameter_name);

CREATE INDEX idx_analysis_results_analysis
ON analysis_results(analysis_id);
```