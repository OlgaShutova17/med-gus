import uuid
from datetime import datetime
from pydantic import BaseModel, field_validator

VALID_STATUSES = ("new", "testing", "confirmed", "rejected")


class CreateHypothesisRequest(BaseModel):
    title: str
    description: str | None = None

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Введите название гипотезы")
        return v


class UpdateHypothesisRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None

    @field_validator("status")
    @classmethod
    def valid_status(cls, v: str | None) -> str | None:
        if v is not None and v not in VALID_STATUSES:
            raise ValueError(f"status must be one of: {', '.join(VALID_STATUSES)}")
        return v


class HypothesisResponse(BaseModel):
    id: uuid.UUID
    theme_id: uuid.UUID
    title: str
    description: str | None
    status: str
    created_at: datetime
    updated_at: datetime


class HypothesisListResponse(BaseModel):
    items: list[HypothesisResponse]
    total: int
