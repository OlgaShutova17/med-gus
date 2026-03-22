---
title: ERD от ИИ
order: 1
---

## Основные сущности

## User

Пользователь системы.

```
User
[tab:id::]
[/tab]
[tab:email::]
[/tab]
[tab:password_hash::]
[/tab]
[tab:name::]
[/tab]
[tab:gender::]
[/tab]
[tab:birth_date::]
[/tab]
[tab:created_at::]
```

Связи

```
User 1 --- N Themes
User 1 --- N Events
User 1 --- N Files
```

---

## Theme (Тематика / проблема)

Главная сущность продукта.

```
Theme
[/tab]
[tab:id::]
[/tab]
[tab:user_id::]
[/tab]
[tab:title::]
[/tab]
[tab:description::]
[/tab]
[tab:created_at::]
```

Связи

```
Theme 1 --- N Hypothesis
Theme 1 --- N Events
Theme 1 --- N Symptoms
Theme 1 --- N TreatmentCourses
```

---

## Hypothesis

Гипотеза причины проблемы.

```
Hypothesis
[/tab]
[tab:id::]
[/tab]
[tab:theme_id::]
[/tab]
[tab:title::]
[/tab]
[tab:description::]
[/tab]
[tab:status::]
[/tab]
[tab:created_at::]
```

Статусы

```
new
testing
confirmed
rejected
```

Связи

```
Hypothesis 1 --- N Events
Hypothesis 1 --- N TreatmentCourses
```

---

## Event (универсальная сущность)

Общее понятие события.

Типы:

* consultation

* analysis

* research

* other

```
Event
[/tab]
[tab:id::]
[/tab]
[tab:user_id::]
[/tab]
[tab:theme_id::]
[/tab]
[tab:hypothesis_id (nullable)::]
[/tab]
[tab:type::]
[/tab]
[tab:date::]
[/tab]
[tab:title::]
[/tab]
[tab:notes::]
[/tab]
[tab:created_at::]
```

Связи

```
Event 1 --- N Files
Event 1 --- 1 Resolution
```

---

## Consultation

Детали консультации врача.

```
Consultation
[/tab]
[tab:id::]
[/tab]
[tab:event_id::]
[/tab]
[tab:clinic::]
[/tab]
[tab:doctor_name::]
[/tab]
[tab:anamnesis_life::]
[/tab]
[tab:anamnesis_disease::]
[/tab]
[tab:diagnosis::]
[/tab]
[tab:treatment::]
[/tab]
[tab:recommendations::]
[/tab]
[tab:follow_up_date::]
```

---

## Analysis

Анализ (например кровь).

```
Analysis
[/tab]
[tab:id::]
[/tab]
[tab:event_id::]
[/tab]
[tab:analysis_type::]
[/tab]
[tab:lab_name::]
[/tab]
[tab:date::]
```

---

## AnalysisParameter

Отдельный показатель анализа.

```
AnalysisParameter
[/tab]
[tab:id::]
[/tab]
[tab:analysis_id::]
[/tab]
[tab:parameter_name::]
[/tab]
[tab:value::]
[/tab]
[tab:unit::]
[/tab]
[tab:reference_min::]
[/tab]
[tab:reference_max::]
```

Связи

```
Analysis 1 --- N AnalysisParameters
```

---

## Research

Инструментальное исследование.

```
Research
[/tab]
[tab:id::]
[/tab]
[tab:event_id::]
[/tab]
[tab:research_type::]
[/tab]
[tab:result_text::]
[/tab]
[tab:findings::]
[/tab]
[tab:recommendations::]
```

---

## TreatmentCourse

Курс лечения.

```
TreatmentCourse
[/tab]
[tab:id::]
[/tab]
[tab:hypothesis_id::]
[/tab]
[tab:doctor::]
[/tab]
[tab:diagnosis::]
[/tab]
[tab:start_date::]
[/tab]
[tab:end_date::]
[/tab]
[tab:result::]
```

---

## Medication

Препарат курса лечения.

```
Medication
[/tab]
[tab:id::]
[/tab]
[tab:course_id::]
[/tab]
[tab:name::]
[/tab]
[tab:dosage::]
[/tab]
[tab:frequency::]
```

---

## Resolution

Субъективная оценка события. ГУСЬМЕД

```
Resolution
[/tab]
[tab:id::]
[/tab]
[tab:event_id::]
[/tab]
[tab:result (helped / not_helped)::]
[/tab]
[tab:comment::]
[/tab]
[tab:created_at::]
```

---

## File

Прикрепленные документы.

```
File
[/tab]
[tab:id::]
[/tab]
[tab:user_id::]
[/tab]
[tab:event_id::]
[/tab]
[tab:file_url::]
[/tab]
[tab:file_type::]
[/tab]
[tab:uploaded_at::]
```

---

## Symptom

Симптомы пользователя.

```
Symptom
[/tab]
[tab:id::]
[/tab]
[tab:theme_id::]
[/tab]
[tab:name::]
[/tab]
[tab:description::]
[/tab]
[tab:date::]
```

---

## 3. ER-диаграмма (упрощенная)

```
User
 |
 | 1:N
 |
Theme
 |
 | 1:N
 |
Hypothesis
 |
 | 1:N
 |
TreatmentCourse
 |
 | 1:N
 |
Medication


Theme
 |
 | 1:N
 |
Event
 |
 |--- Consultation
 |
 |--- Analysis --- AnalysisParameter
 |
 |--- Research
 |
 |--- Other


Event
 |
 | 1:1
 |
Resolution


Event
 |
 | 1:N
 |
Files
```

---

## 4. Особенность модели (ключевая идея продукта)

Большинство медицинских приложений строятся вокруг:

```
пациент → анализ
```

А здесь модель:

```
пациент
   ↓
проблема (theme)
   ↓
гипотезы
   ↓
события лечения
   ↓
результат
```

Это **уникальная проблемно-ориентированная медицинская история**.

&nbsp;

**Полная схема**

USER
\|
\| 1:N
\|
THEME (проблема)
\|
\| 1:N
\|
HYPOTHESIS
\|
\| 1:N
\|
EVENT
\|
\|---- CONSULTATION
\|---- ANALYSIS
\|         \|
\|         \| 1:N
\|         \|
\|      ANALYSIS\_RESULT
\|
\|---- RESEARCH
\|
\|---- OTHER\_EVENT
\|
\| 1:N
\|
FILE

EVENT
\|
\| 1:1
\|
RESOLUTION

HYPOTHESIS
\|
\| 1:N
\|
TREATMENT\_COURSE
\|
\| 1:N
\|
MEDICATION[/tab]
