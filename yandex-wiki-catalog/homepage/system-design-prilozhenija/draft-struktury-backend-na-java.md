---
title: Draft структуры backend на Java
order: 1
---

Рекомендую стек:

```
Java 21
Spring Boot
PostgreSQL
Hibernate
Redis
Kafka (опционально)
```

---

## High level архитектура

```
Controller
   ↓
Service
   ↓
Domain
   ↓
Repository
   ↓
Database
```

---

## Структура проекта

```
gusmed-backend

src/main/java/com/gusmed
```

---

## core modules

```
auth
users
medical
analyses
hypothesis
timeline
ai
```

---

## Полная структура

```
com.gusmed

config
security
common

users
auth

medical
   parameters
   diseases
   symptoms
   knowledgegraph

analyses
timeline
hypothesis
ai

analytics
```

---

## config

```
config/

DatabaseConfig
SecurityConfig
JacksonConfig
RedisConfig
```

---

## common

Общие классы.

```
common/

BaseEntity
ApiResponse
Exceptions
Utils
Enums
```

---

## users module

```
users/

UserController
UserService
UserRepository

entity/
   User

dto/
   UserDto
```

---

## medical module

Справочники.

```
medical/
```

---

## parameters

```
medical/parameters

ParameterController
ParameterService
ParameterRepository
```

entities:

```
MedicalParameter
ParameterAlias
ReferenceRange
ParameterUnit
```

---

## diseases

```
medical/diseases
```

entities:

```
Disease
DiseaseSymptom
DiseaseParameter
```

---

## symptoms

```
medical/symptoms
```

entity:

```
Symptom
```

---

## knowledge graph

```
medical/knowledgegraph
```

entity:

```
DiseaseRelation
SymptomRelation
ParameterRelation
```

---

## analyses module

Работа с анализами пользователя.

```
analyses/
```

---

структура:

```
analyses

AnalysisController
AnalysisService
AnalysisRepository
```

entities:

```
Analysis
AnalysisResult
AnalysisValue
```

---

## timeline module

История событий пользователя.

```
timeline/
```

entities:

```
TimelineEvent
EventType
```

Типы событий:

```
ANALYSIS
SYMPTOM
VISIT
TREATMENT
NOTE
```

---

## hypothesis module

Медицинское расследование.

```
hypothesis/
```

entities:

```
Problem
Hypothesis
Evidence
HypothesisScore
```

---

## ai module

AI reasoning.

```
ai/
```

services:

```
HypothesisEngine
AnalysisInterpreter
SymptomAnalyzer
```

---

## analytics module

```
analytics/

TrendService
InsightService
```

---

## пример entity

MedicalParameter:

```
@Entity
public class MedicalParameter {

    @Id
    private UUID id;

    private String code;

    private String name;

    private String category;

}
```

---

## example repository

```
@Repository
public interface ParameterRepository
        extends JpaRepository<MedicalParameter, UUID> {

    Optional[MedicalParameter](MedicalParameter) findByCode(String code);

}
```

---

## example service

```
@Service
public class ParameterService {

    private final ParameterRepository repository;

    public ParameterService(ParameterRepository repository) {
        this.repository = repository;
    }

    public MedicalParameter getByCode(String code) {
        return repository.findByCode(code)
            .orElseThrow();
    }

}
```

---

## example controller

```
@RestController
@RequestMapping("/api/parameters")
public class ParameterController {

    private final ParameterService service;

    @GetMapping("/{code}")
    public MedicalParameter get(@PathVariable String code) {
        return service.getByCode(code);
    }

}
```

---

## будущие сервисы

```
OCR Service
Document Parser
AI Interpreter
Knowledge Graph Reasoner
```

---

## event architecture (рекомендую)

Очень полезно.

```
analysis_uploaded
analysis_parsed
hypothesis_updated
```

Можно сделать через:

```
Kafka
или
Spring Events
```

---

## Infrastructure

```
PostgreSQL
Redis
S3 (storage анализов)
OpenSearch (поиск)
```

---

## Deployment

```
Docker
Kubernetes (позже)
```