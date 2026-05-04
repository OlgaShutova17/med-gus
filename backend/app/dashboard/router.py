import uuid
from fastapi import APIRouter, Depends

from app.dependencies import get_db, get_current_user
from app.dashboard import service

router = APIRouter(tags=["dashboard"])


@router.get("/dashboard")
async def get_dashboard(
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    return await service.get_dashboard(conn, user_id)
