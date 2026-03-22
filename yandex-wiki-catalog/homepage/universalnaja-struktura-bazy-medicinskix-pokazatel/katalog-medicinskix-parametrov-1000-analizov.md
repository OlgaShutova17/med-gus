---
title: Каталог медицинских параметров (1000+ анализов)
order: 1
---

Самая сложная часть медицинских систем — **нормализация анализов**.

Проблема:

один и тот же параметр может называться:

```
Hb
HGB
Hemoglobin
Гемоглобин
Hemoglobine
```

Если не сделать **единый каталог**, AI не сможет анализировать данные.

---

## Архитектура каталога параметров

Нужно разделить **4 уровня**.

```
Analysis
   ↓
Parameter
   ↓
Units
   ↓
Reference ranges
```

---

## 1. Analyses (типы анализов)

Каталог типов анализов.

Примеры:

```
Общий анализ крови
Биохимия крови
Гормоны
Анализ мочи
```

### таблица

```
analyses
```

```
id
name
category
description
```

category:

```
blood
urine
hormone
vitamin
```

---

## 2. Medical Parameters

Каталог **всех медицинских показателей**.

Примеры:

```
HEMOGLOBIN
FERRITIN
GLUCOSE
TSH
VITAMIN_D
```

### таблица

```
medical_parameters
```

```
id
code
name
category
description
```

category:

```
hematology
biochemistry
hormones
vitamins
```

---

## 3. Parameter aliases

Список всех названий.

### таблица

```
parameter_aliases
```

```
id
parameter_id
alias
language
```

Пример:

```
parameter_id: HEMOGLOBIN

aliases:

Hb
HGB
Гемоглобин
Hemoglobin
```

Это используется при **AI parsing анализов**.

---

## 4. Units

Разные лаборатории используют разные единицы.

Пример:

```
г/л
g/L
g/dL
```

### таблица

```
parameter_units
```

```
id
parameter_id
unit
conversion_factor
```

Пример:

```
g/dL → g/L
factor = 10
```

---

## 5. Reference ranges

Нормы зависят от:

```
возраст
пол
единицы
```

### таблица

```
reference_ranges
```

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

## Пример записи

```
parameter: HEMOGLOBIN
sex: male
age: 18-60
range: 130–170 g/L
```

---

## 6. Связь анализа и параметров

Не все параметры входят в каждый анализ.

### таблица

```
analysis_parameters
```

```
analysis_id
parameter_id
```

---

## Пример

```
Общий анализ крови:

HEMOGLOBIN
ERYTHROCYTES
LEUKOCYTES
PLATELETS
```

---

## 7. User results

Когда пользователь загружает анализ:

```
analysis_results
```

```
id
user_id
analysis_id
date
lab_name
```

---

## 8. Значения параметров

```
analysis_values
```

```
analysis_result_id
parameter_id
value
unit
status
```

status:

```
low
normal
high
```

---

## Как работает parsing анализа

Пример входа:

```
Гемоглобин 120 г/л
Ферритин 10 мкг/л
```

AI pipeline:

```
OCR
↓
text
↓
parameter alias match
↓
normalize parameter
↓
convert unit
↓
save value
```

---

## В итоге

```
Гемоглобин
Hb
HGB
```

все превращаются в

```
HEMOGLOBIN
```

Это **критично для аналитики**.

---

## Размер каталога

Типичный каталог:

```
500 анализов
4000 параметров
15000 aliases
```