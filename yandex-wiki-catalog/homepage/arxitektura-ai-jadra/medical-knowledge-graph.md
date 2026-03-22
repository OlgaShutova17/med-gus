---
title: Medical Knowledge Graph
order: 1
---

Это **самая мощная часть системы**.

Она позволяет AI:

```
понимать медицину
```

---

## Основные сущности графа

```
Symptom
Parameter
Disease
Treatment
Drug
```

---

## Типы связей

```
symptom → disease
parameter → disease
disease → treatment
drug → disease
```

---

## Пример фрагмента графа

```
усталость
     │
     │
     ▼
железодефицитная анемия
     │
     │
     ▼
низкий ферритин
```

---

## Более полный пример

```
Symptom

усталость
головокружение
слабость

      │
      ▼

Disease

железодефицитная анемия

      │
      ▼

Analysis

ферритин ↓
гемоглобин ↓

      │
      ▼

Treatment

препараты железа
```

---

## Таблицы Knowledge Graph

## diseases

```
id
name
icd_code
description
```

---

## symptom\_disease

```
symptom_id
disease_id
weight
```

weight:

```
вероятность связи
```

---

## parameter\_disease

```
parameter_id
disease_id
weight
direction
```

direction:

```
high
low
```

---

## disease\_treatment

```
disease_id
treatment_id
effectiveness_score
```

---

## Как работает AI reasoning

AI получает:

```
симптомы
анализы
историю
```

Пример:

```
усталость
головокружение
ферритин 10
```

AI ищет в графе:

```
усталость → железодефицит
ферритин↓ → железодефицит
```

---

## Расчёт вероятности

```
score =

symptom_weight
+
analysis_weight
+
history_weight
```

---

## Пример результата

```
дефицит железа — 72%
гипотиреоз — 15%
депрессия — 13%
```

---

## Следующий шаг reasoning

AI предлагает:

```
следующие тесты
```

Например:

```
проверить TSH
проверить витамин B12
```

---

## Почему Knowledge Graph важен

Без него AI делает:

```
только LLM ответы
```

С графом:

```
структурированная медицина
```

---

## Архитектура AI reasoning

```
User data
     │
     ▼
Normalization
     │
     ▼
Knowledge Graph
     │
     ▼
Reasoning Engine
     │
     ▼
Insights
```

---

## Где хранить граф

Можно:

```
PostgreSQL
```

или

```
Neo4j
```

Для MVP достаточно:

```
Postgres
```

---

## Самая сильная фича

Со временем система может находить:

```
скрытые паттерны
```

Например:

```
мигрени → плохой сон → стресс
```

---

## Почему это может стать большим продуктом

Система будет хранить:

```
симптомы
анализы
лечение
результаты
```

Это создаёт:

```
уникальный medical dataset
```