# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a **documentation-only repository** for a medical health tracking application (МедДневник). There is no source code — only architecture specifications, database schemas, API contracts, and product documentation.

## Repository Structure

Documentation lives under `yandex-wiki-catalog/homepage/`:

| Directory | Content |
|---|---|
| `overview/` | Project overview, requirements, glossary, functional modules |
| `use-cases/` | 10 standardized use case files (User Story → GWT format) |
| `api-endpoints-rest/` | REST API specification (`/api/v1`) |
| `struktura-tablic/` | PostgreSQL DDL — `db-mvp.md` (MVP schema) + `_index.md` (full schema) |
| `system-design-prilozhenija/` | System design — `system-design-mvp.md` (MVP) + `_index.md` (full) + `struktura-back-end.md` + `scaling-architecture.md` |
| `ux-koncepcija-silnogo-health-tech-produkta/` | `ux-concept-ba.md` (UX for BA) + `ux-figma-prompt.md` (Figma AI prompt) |
| `arxitektura-ai-jadra/` | AI pipeline architecture + Medical Knowledge Graph |
| `universalnaja-struktura-bazy-medicinskix-pokazatel/` | Medical parameters catalog (1000+ analyses, LOINC/SNOMED) |
| `intervju/` | User interview findings |
| `roadmap.md` | 12-week MVP roadmap |

Root: `gramax.config.yaml` — Gramax wiki configuration.

## Product Architecture

**Unique data model** — problem-oriented medical record:

```
User → Theme (health problem) → Hypotheses → Events (consultations/analyses/research) → Resolution
```

**System architecture:** Modular monolith + separate AI service

```
Web App (Next.js) / Telegram Bot
        ↓ HTTPS
    API Gateway
    ├── Backend API (FastAPI/Python) — PostgreSQL, Redis, MinIO (S3)
    └── AI Service — OCR → Medical NLP → Knowledge Graph → Insight Generator
```

## Planned Tech Stack

- **Backend:** FastAPI (Python)
- **Frontend:** Next.js
- **Database:** PostgreSQL (with `pgvector` for AI embeddings)
- **Object Storage:** MinIO
- **Cache:** Redis
- **OCR:** Tesseract OCR (AWS Textract for production)
- **Vector DB:** pgvector / Weaviate / Pinecone

## Core Domain Concepts

- **Theme** — a specific health problem a user is investigating
- **Hypothesis** — a proposed cause for a theme (statuses: `new`, `testing`, `confirmed`, `rejected`)
- **Event** — a timestamped action on a theme (types: `consultation`, `analysis`, `research`, `other`)
- **Resolution** — outcome of an event (`helped` / `not_helped`)
- **Timeline** — the primary UI pattern: `GET /themes/{id}/timeline` aggregates all events chronologically

## Key API Patterns

Base path: `/api/v1`

- Auth: JWT with access + refresh tokens
- All data is user-scoped (row-level security is a hard requirement)
- Analysis dynamics endpoint: `GET /analysis-results/dynamics` — core analytics feature
- AI endpoints: `POST /ai/analyze-analysis`, `POST /ai/chat`, `POST /ai/recommend-specialist`

## AI Pipeline (Document → Insights)

1. User uploads PDF/photo → MinIO storage
2. OCR extracts text
3. Medical NLP parses parameters, values, units, reference ranges
4. Normalization engine standardizes parameter names (multi-language: ru/en/latin)
5. Knowledge graph maps symptoms → diseases → treatments
6. Reasoning engine scores risks and detects patterns
7. Insight generator produces patient-friendly recommendations

## DB Schema Split

- **MVP** (`struktura-tablic/db-mvp.md`): `analysis_results` stores `parameter_name TEXT` — no catalog linkage
- **Full** (`struktura-tablic/_index.md`): adds `medical_parameters` catalog, `parameter_aliases`, `reference_ranges`, Knowledge Graph tables (`diseases`, `symptom_disease`, `analysis_disease`, `treatment_disease`)
