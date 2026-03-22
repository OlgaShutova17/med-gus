---
title: Полная ER-диаграмма системы
order: 1
---

## Основные домены системы

```
Users
Problems (Themes)
Events
Medical Data
AI Knowledge
Treatment
Files
```

---

## USERS

### users

```
id (uuid)
email
password_hash
name
birth_date
sex
created_at
```

---

### user\_profiles

```
id
user_id
height
weight
blood_type
chronic_conditions
allergies
```

---

## PROBLEMS (Themes)

### themes

Проблема пользователя.

```
id
user_id
title
description
status
created_at
```

---

### theme\_symptoms

```
id
theme_id
symptom_id
severity
created_at
```

---

## SYMPTOMS

### symptoms

```
id
name
description
```

---

## HYPOTHESES

### hypotheses

```
id
theme_id
title
description
status
created_at
```

status:

```
testing
confirmed
rejected
```

---

## EVENTS

Все действия пользователя — события.

### events

```
id
theme_id
event_type
title
description
event_date
created_at
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

## CONSULTATIONS

### consultations

```
id
event_id
doctor_specialization
clinic
diagnosis
recommendations
```

---

## RESEARCH

### researches

```
id
event_id
research_type
result_summary
```

Пример:

```
МРТ
КТ
УЗИ
```

---

## ANALYSES

### analyses

Тип анализа.

```
id
name
category
description
```

---

### analysis\_results

Результат анализа пользователя.

```
id
event_id
analysis_id
lab_name
result_date
source_file_id
```

---

### analysis\_values

Значения параметров.

```
id
analysis_result_id
parameter_id
value
unit
reference_min
reference_max
status
```

status:

```
low
normal
high
```

---

## MEDICAL PARAMETERS

### medical\_parameters

```
id
code
name
category
description
```

Примеры:

```
HEMOGLOBIN
GLUCOSE
FERRITIN
```

---

### parameter\_aliases

```
id
parameter_id
alias
language
```

---

### parameter\_units

```
id
parameter_id
unit
conversion_factor
```

---

### reference\_ranges

```
id
parameter_id
sex
age_min
age_max
min_value
max_value
unit
```

---

## TREATMENT

### treatments

```
id
theme_id
title
description
start_date
end_date
```

---

### medications

```
id
treatment_id
drug_id
dosage
frequency
```

---

### drugs

```
id
name
active_substance
```

---

## FILE STORAGE

### files

```
id
user_id
file_type
storage_url
created_at
```

---

### file\_links

Связь файла с объектами.

```
id
file_id
entity_type
entity_id
```

---

## AI INSIGHTS

### ai\_insights

```
id
user_id
theme_id
insight_type
content
created_at
```

---

### ai\_recommendations

```
id
insight_id
recommendation_type
content
priority
```

---

## KNOWLEDGE GRAPH

### diseases

```
id
name
icd_code
description
```

---

### symptom\_disease

```
symptom_id
disease_id
weight
```

---

### analysis\_disease

```
parameter_id
disease_id
weight
```

---

### treatment\_disease

```
treatment_id
disease_id
effectiveness
```

---

## Упрощённая схема связей

```
User
 └── Themes
      ├── Hypotheses
      ├── Symptoms
      └── Events
           ├── Consultations
           ├── Analyses
           │     └── Analysis Values
           ├── Research
           └── Treatments
```