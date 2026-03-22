# МедДневник — Проектная документация

Репозиторий содержит проектную документацию продукта: веб-приложения для проблемно-ориентированного ведения медицинской истории с AI-агентом.

---

## О продукте

**МедДневник** помогает пользователю ответить на вопрос *«Почему мне плохо?»* — не просто хранить анализы и документы, а вести структурированное расследование конкретной проблемы со здоровьем.

Центральная модель: **Проблема → Гипотезы → События → Доказательства → Вывод**

---

## Структура документации

```
yandex-wiki-catalog/homepage/
│
├── overview/                        # О проекте
├── use-cases/                       # Пользовательские сценарии
├── api-endpoints-rest/              # REST API
├── struktura-tablic/                # Схема базы данных
├── system-design-prilozhenija/      # Архитектура системы
├── ux-koncepcija-silnogo-health-tech-produkta/  # UX-концепция
├── arxitektura-ai-jadra/            # AI-ядро
├── universalnaja-struktura-bazy-medicinskix-pokazatel/  # Каталог медпараметров
├── intervju/                        # Результаты интервью
└── roadmap.md                       # Дорожная карта
```

---

## О проекте

| Файл | Описание |
|---|---|
| [О проекте, требования](yandex-wiki-catalog/homepage/overview/project-overview.md) | Описание продукта, AS IS / TO BE, 14 функциональных и 5 нефункциональных требований, фичи на будущее |
| [Функциональные модули](yandex-wiki-catalog/homepage/overview/features.md) | Карта функциональности по 8 модулям с разбивкой на фронт / бэк / БД |
| [Глоссарий](yandex-wiki-catalog/homepage/overview/glossary.md) | 13 доменных терминов проекта: тематика, событие, гипотеза, резолюция и др. |

---

## Пользовательские сценарии (Use Cases)

Все сценарии оформлены в единой структуре: User Story → Приоритет → Предусловия → Бизнес-правила → Основной сценарий → Альтернативы → Критерии приёмки → GWT.

| Файл | Сценарий |
|---|---|
| [uc-theme.md](yandex-wiki-catalog/homepage/use-cases/uc-theme.md) | Создание тематики (проблемы) |
| [uc-hypothesis.md](yandex-wiki-catalog/homepage/use-cases/uc-hypothesis.md) | Добавление гипотезы причины |
| [uc-consultation.md](yandex-wiki-catalog/homepage/use-cases/uc-consultation.md) | Добавление консультации специалиста |
| [uc-analysis-file.md](yandex-wiki-catalog/homepage/use-cases/uc-analysis-file.md) | Загрузка анализа файлом (PDF / фото) |
| [uc-analysis-manual.md](yandex-wiki-catalog/homepage/use-cases/uc-analysis-manual.md) | Ручной ввод результатов анализа |
| [uc-analysis-ai.md](yandex-wiki-catalog/homepage/use-cases/uc-analysis-ai.md) | AI-обработка: OCR → NLP → верификация → инсайты |
| [uc-research.md](yandex-wiki-catalog/homepage/use-cases/uc-research.md) | Добавление результата исследования (МРТ, КТ, УЗИ) |
| [uc-treatment.md](yandex-wiki-catalog/homepage/use-cases/uc-treatment.md) | Создание и отслеживание курса лечения |
| [uc-resolution.md](yandex-wiki-catalog/homepage/use-cases/uc-resolution.md) | Выбор резолюции «Помогло» / «Не помогло» |
| [uc-dynamics.md](yandex-wiki-catalog/homepage/use-cases/uc-dynamics.md) | Просмотр динамики анализов на графике |

---

## REST API

| Файл | Описание |
|---|---|
| [API Endpoints](yandex-wiki-catalog/homepage/api-endpoints-rest/_index.md) | Полный список эндпоинтов: auth, themes, hypotheses, events, analyses, AI, dashboard. Базовый путь `/api/v1` |

---

## База данных

| Файл | Описание |
|---|---|
| [Схема MVP](yandex-wiki-catalog/homepage/struktura-tablic/db-mvp.md) | Минимальная схема для запуска: core-таблицы, параметры анализов текстом. Таблица роста — что добавляется после MVP |
| [Целевая схема](yandex-wiki-catalog/homepage/struktura-tablic/_index.md) | Полная схема: ER-диаграмма, все таблицы включая справочник медпараметров, Knowledge Graph, AI-инсайты |

---

## Архитектура системы

| Файл | Описание |
|---|---|
| [System Design MVP](yandex-wiki-catalog/homepage/system-design-prilozhenija/system-design-mvp.md) | MVP: стек (FastAPI / Next.js / PostgreSQL / MinIO / Redis), 1 сервер на Docker Compose, data flow анализа, ограничения |
| [System Design (полный)](yandex-wiki-catalog/homepage/system-design-prilozhenija/_index.md) | Полная архитектура: модульный монолит + AI-сервис, все модули backend, AI-пайплайн, Knowledge Graph, Vector DB, RAG |
| [Структура backend](yandex-wiki-catalog/homepage/system-design-prilozhenija/struktura-back-end.md) | Слои кода (API / Services / Domain / Infrastructure), модули, структура директорий, AI-модуль |
| [Архитектура масштабирования](yandex-wiki-catalog/homepage/system-design-prilozhenija/scaling-architecture.md) | Три стадии роста: MVP → Product-Market Fit → Growth; микросервисы, Event Bus, ClickHouse, интеграции |

---

## UX-концепция

| Файл | Описание |
|---|---|
| [Концепция (для BA)](yandex-wiki-catalog/homepage/ux-koncepcija-silnogo-health-tech-produkta/ux-concept-ba.md) | Философия UX, информационная архитектура, дуальная модель (Timeline + Гипотезы), 5 killer-функций, user journey, принципы |
| [Промпт для Figma AI](yandex-wiki-catalog/homepage/ux-koncepcija-silnogo-health-tech-produkta/ux-figma-prompt.md) | Готовый промпт для Figma AI-агента: design system, цвета, типографика, спецификации 7 экранов, 14 компонентов, states |

---

## AI-ядро

| Файл | Описание |
|---|---|
| [Архитектура AI](yandex-wiki-catalog/homepage/arxitektura-ai-jadra/_index.md) | Полный AI-пайплайн: OCR → Med NLP → нормализация → Knowledge Graph → Reasoning → инсайты. Сервисы и технологии |
| [Medical Knowledge Graph](yandex-wiki-catalog/homepage/arxitektura-ai-jadra/medical-knowledge-graph.md) | Граф медицинских знаний: сущности, типы связей, алгоритм вычисления вероятности гипотез, таблицы БД |

---

## Каталог медицинских параметров

| Файл | Описание |
|---|---|
| [Структура каталога](yandex-wiki-catalog/homepage/universalnaja-struktura-bazy-medicinskix-pokazatel/_index.md) | Архитектура справочника: 4 уровня (Анализ → Параметр → Единицы → Нормы), таблицы, цепочка разбора |
| [Каталог: 1000+ анализов](yandex-wiki-catalog/homepage/universalnaja-struktura-bazy-medicinskix-pokazatel/katalog-medicinskix-parametrov-1000-analizov.md) | Нормализация названий (Hb / HGB / Гемоглобин → HEMOGLOBIN), пайплайн разбора, масштаб: 500 анализов / 4000 параметров / 15000 псевдонимов |
| [Наполнение каталога](yandex-wiki-catalog/homepage/universalnaja-struktura-bazy-medicinskix-pokazatel/kak-napolnit-bazu-med-pokazatelejj.md) | Источники данных: LOINC, SNOMED CT, ICD-10, HPO, OpenFDA, нормы Mayo Clinic / LabCorp / NHS. ETL-стратегия |

---

## Исследование пользователей

| Файл | Описание |
|---|---|
| [Результаты интервью](yandex-wiki-catalog/homepage/intervju/user-interview-findings.md) | Потребности пользователей: систематизация анализов, хронология событий, интерпретация результатов с AI |

---

## Дорожная карта

| Файл | Описание |
|---|---|
| [Roadmap](yandex-wiki-catalog/homepage/roadmap.md) | 12-недельный план разработки MVP: месяц 1 — core, месяц 2 — медданные, месяц 3 — AI-функции |

---

## Деплой

| Файл | Описание |
|---|---|
| [Деплой MVP на Selectel](yandex-wiki-catalog/homepage/deployment/selectel-mvp.md) | Пошаговая инструкция: PostgreSQL + FastAPI backend (auth + themes) + Next.js frontend на одном сервере через Docker Compose |

---

## Ключевая идея продукта

Большинство медицинских приложений организуют данные как:

```
Пациент → Анализ
```

Этот продукт использует проблемно-ориентированную модель:

```
Пациент
  └── Проблема (Тематика)
        ├── Гипотезы
        └── События → Резолюции
```

Это позволяет видеть не набор файлов, а **полное расследование** конкретной проблемы со здоровьем.
