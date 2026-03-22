---
title: Как наполнить базу мед показателей
order: 1
---

Есть **3 типа источников**:

```
1. медицинские классификаторы
2. open medical datasets
3. clinical guidelines
```

Лучше комбинировать.

---

## 1. LOINC — главный стандарт лабораторных тестов

Это **де-факто мировой стандарт лабораторных анализов**.

Содержит:

```
100 000+ лабораторных тестов
```

Пример записи:

```
LOINC: 718-7
Hemoglobin [Mass/volume] in Blood
Unit: g/dL
```

Можно получить:

```
test name
unit
description
method
```

Что использовать:

```
LOINC code → parameter code
LOINC name → parameter name
```

Пример записи в базе:

```
code: HEMOGLOBIN
loinc_code: 718-7
name: Hemoglobin
category: hematology
```

---

Источник:

[https://loinc.org/downloads/](https://loinc.org/downloads/)

Формат:

```
CSV
```

---

## 2. SNOMED CT

Гигантская медицинская ontology.

Используется для:

```
symptoms
diseases
procedures
```

Пример:

```
Fatigue
SCTID: 84229001
```

Можно использовать для:

```
symptoms
diseases
relations
```

---

Источник:

[https://www.snomed.org](https://www.snomed.org)

Но:

```
нужна лицензия
```

Для MVP можно использовать альтернативы.

---

## 3. ICD-10

Классификатор болезней.

Используется:

```
diseases
diagnosis codes
```

Пример:

```
E61.1
Iron deficiency
```

---

Источник:

[https://icd.who.int/](https://icd.who.int/)

---

## 4. OpenFDA

Полезно для:

```
drugs
drug interactions
```

Источник:

[https://open.fda.gov](https://open.fda.gov)

---

## 5. Human Phenotype Ontology (HPO)

Очень хороший источник симптомов.

Пример:

```
HP:0012378
Fatigue
```

---

Источник:

https://hpo.jax.org/app/download/ontology

---

## 6. Reference ranges

Нормы можно взять из:

Clinical sources:

```
Mayo Clinic Labs
LabCorp
NHS reference ranges
```

или datasets:

```
NHANES
```

---

## MVP стратегия наполнения

Лучше сделать pipeline:

```
LOINC → parameters
HPO → symptoms
ICD10 → diseases
```

---

## Пример MVP каталога

```
parameters: 2000
symptoms: 500
diseases: 1500
```

Этого более чем достаточно.

---

## Data ingestion pipeline

Скрипт загрузки:

```
raw datasets
 ↓
ETL scripts
 ↓
normalized tables
 ↓
postgres
```

---

## Пример ingestion pipeline

```
datasets/
   loinc.csv
   hpo.obo
   icd10.csv

scripts/
   load_loinc.py
   load_icd.py
   load_hpo.py
```