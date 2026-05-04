import uuid
from fastapi import APIRouter, Depends, HTTPException, status

from app.dependencies import get_db, get_current_user
from app.themes.schemas import (
    CreateThemeRequest,
    UpdateThemeRequest,
    ThemeResponse,
    ThemeListResponse,
)
from app.themes import service

router = APIRouter(prefix="/themes", tags=["themes"])


@router.get("", response_model=ThemeListResponse)
async def list_themes(
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    items = await service.get_themes(conn, user_id)
    return ThemeListResponse(items=items, total=len(items))


@router.post("", response_model=ThemeResponse, status_code=status.HTTP_201_CREATED)
async def create_theme(
    body: CreateThemeRequest,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    theme = await service.create_theme(conn, user_id, body.title, body.description)
    return theme


@router.get("/{theme_id}", response_model=ThemeResponse)
async def get_theme(
    theme_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    theme = await service.get_theme(conn, theme_id, user_id)
    if not theme:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Theme not found")
    return theme


@router.patch("/{theme_id}", response_model=ThemeResponse)
async def update_theme(
    theme_id: uuid.UUID,
    body: UpdateThemeRequest,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    theme = await service.update_theme(
        conn, theme_id, user_id, body.title, body.description, body.status
    )
    if not theme:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Theme not found")
    return theme


@router.delete("/{theme_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_theme(
    theme_id: uuid.UUID,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    deleted = await service.delete_theme(conn, theme_id, user_id)
    if not deleted:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Theme not found")
