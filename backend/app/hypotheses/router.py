import uuid
from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_db, get_current_user
from app.hypotheses.schemas import (
    CreateHypothesisRequest,
    UpdateHypothesisRequest,
    HypothesisResponse,
    HypothesisListResponse,
)
from app.hypotheses import service

router = APIRouter(tags=["hypotheses"])


# ── scoped under /themes/{theme_id}/hypotheses ──────────────────────────────

@router.get("/themes/{theme_id}/hypotheses", response_model=HypothesisListResponse)
async def list_hypotheses(
    theme_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    items = await service.get_hypotheses(conn, theme_id, user_id)
    return HypothesisListResponse(items=items, total=len(items))


@router.post(
    "/themes/{theme_id}/hypotheses",
    response_model=HypothesisResponse,
    status_code=status.HTTP_201_CREATED,
)
async def create_hypothesis(
    theme_id: uuid.UUID,
    body: CreateHypothesisRequest,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    # verify theme ownership
    theme = await conn.fetchrow(
        "SELECT id FROM themes WHERE id = $1 AND user_id = $2", theme_id, user_id
    )
    if not theme:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Theme not found")

    hypothesis = await service.create_hypothesis(
        conn, theme_id, user_id, body.title, body.description
    )
    return hypothesis


# ── scoped under /hypotheses/{id} ───────────────────────────────────────────

@router.patch("/hypotheses/{hypothesis_id}", response_model=HypothesisResponse)
async def update_hypothesis(
    hypothesis_id: uuid.UUID,
    body: UpdateHypothesisRequest,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    hypothesis = await service.update_hypothesis(
        conn, hypothesis_id, user_id, body.title, body.description, body.status
    )
    if not hypothesis:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Hypothesis not found")
    return hypothesis


@router.delete("/hypotheses/{hypothesis_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_hypothesis(
    hypothesis_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    deleted = await service.delete_hypothesis(conn, hypothesis_id, user_id)
    if not deleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Hypothesis not found")
