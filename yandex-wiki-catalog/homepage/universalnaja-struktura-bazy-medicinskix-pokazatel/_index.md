---
title: Универсальная структура базы медицинских показателей
order: 1
---

Нужно поддерживать:

```
2000+ анализов
10000+ параметров
```

---

## Основные таблицы

## medical\_parameters

Справочник показателей.

```
id
code
name
category
description
```

Пример:

```
HEMOGLOBIN
FERRITIN
GLUCOSE
```

---

## parameter\_aliases

Разные названия параметра.

```
id
parameter_id
alias
language
```

Пример:

```
Hb
HGB
Гемоглобин
```

---

## parameter\_units

Допустимые единицы.

```
id
parameter_id
unit
conversion_factor
```

Пример:

```
g/L
g/dL
```

---

## reference\_ranges

Нормы показателей.

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

## analyses

Тип анализа.

```
id
name
category
description
```

Пример:

```
общий анализ крови
биохимия крови
гормоны
```

---

## analysis\_parameters

Связь анализа и параметров.

```
analysis_id
parameter_id
```

---

## user\_analysis\_results

Результаты пользователя.

```
id
user_id
analysis_id
date
source_file
```

---

## analysis\_values

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

Статус:

```
low
normal
high
```

---

## Структура хранения динамики

История хранится автоматически.

Пример:

```
analysis_values
```

```
date
parameter
value
```

Позволяет строить:

```
графики
динамику
тренды
```

---

## Дополнительные медицинские таблицы

## symptoms

```
id
name
description
```

---

## diseases

```
id
name
icd_code
description
```

---

## treatments

```
id
name
description
```

---

## drugs

```
id
name
active_substance
```

---

## Knowledge Graph таблицы

## symptom\_disease

```
symptom_id
disease_id
weight
```

---

## analysis\_disease

```
parameter_id
disease_id
weight
```

---

## treatment\_disease

```
treatment_id
disease_id
effectiveness
```

---

## Пример связей

```
симптом
 ↓
анализ
 ↓
диагноз
 ↓
лечение
```