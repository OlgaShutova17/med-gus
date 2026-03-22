# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This is a **documentation-only repository** — a Gramax wiki export from Yandex Wiki for a medical health tracking application (MVP). There is no source code here; the repository contains architecture specifications, database schemas, API contracts, and product documentation.

## Repository Structure

Documentation lives under `yandex-wiki-catalog/homepage/`:

| Directory | Content |
|---|---|
| `44cddbb2914f/` | Project overview, functional & non-functional requirements |
| `2a35726b4c5c/` | Entity-Relationship Diagram & database schema |
| `1c63384ca8de/` | User stories & implementation guides (11 docs) |
| `api-endpoints-rest/` | REST API specification (`/api/v1`) |
| `arxitektura-ai-jadra/` | AI pipeline architecture |
| `struktura-tablic/` | PostgreSQL DDL with indexes |
| `system-design-prilozhenija/` | System design & deployment architecture |
| `ux-koncepcija-*/` | UX concept & wireframes |
| `road-map-proekta.md` | 12-week MVP roadmap |
| `glossarijj.md` | Domain glossary |

`gramax.config.yaml` — Gramax wiki import configuration (Yandex Wiki credentials).

## Product Architecture

**Unique data model** — problem-oriented medical record (not generic analysis storage):

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
- All data is user-scoped (data segregation is a hard requirement)
- Analysis dynamics endpoint: `GET /analysis-results/dynamics` — core analytics feature
- AI endpoints: `POST /ai/analyze-analysis`, `POST /ai/recommend-specialist`

## AI Pipeline (Document → Insights)

1. User uploads PDF/photo → MinIO storage
2. OCR extracts text
3. Medical NLP parses parameters, values, units, reference ranges
4. Normalization engine standardizes parameter names (multi-language)
5. Knowledge graph maps symptoms → diseases → treatments
6. Reasoning engine scores risks and detects patterns
7. Insight generator produces patient-friendly recommendations
