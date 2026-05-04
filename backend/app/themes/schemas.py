import uuid
from datetime import datetime
from pydantic import BaseModel, field_validator


class CreateThemeRequest(BaseModel):
    title: str
    description: str | None = None

    @field_validator("title")
    @classmethod
    def title_not_empty(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Введите название тематики")
        return v


class UpdateThemeRequest(BaseModel):
    title: str | None = None
    description: str | None = None
    status: str | None = None

    @field_validator("status")
    @classmethod
    def valid_status(cls, v: str | None) -> str | None:
        if v is not None and v not in ("active", "resolved", "archived"):
            raise ValueError("status must be active | resolved | archived")
        return v


class ThemeResponse(BaseModel):
    id: uuid.UUID
    title: str
    description: str | None
    status: str
    created_at: datetime
    updated_at: datetime
    hypotheses_count: int = 0
    confirmed_hypothesis: str | None = None  # title of confirmed/leading hypothesis


class ThemeListResponse(BaseModel):
    items: list[ThemeResponse]
    total: int
