import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import get_db, get_current_user
from app.auth.schemas import (
    RegisterRequest,
    TokenResponse,
    UserResponse,
    UpdateProfileRequest,
)
from app.auth.service import hash_password, verify_password, create_access_token

router = APIRouter(prefix="/auth", tags=["auth"])


@router.post("/register", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def register(body: RegisterRequest, conn=Depends(get_db)):
    existing = await conn.fetchrow("SELECT id FROM users WHERE email = $1", body.email)
    if existing:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Email already registered")

    user_id = await conn.fetchval(
        """
        INSERT INTO users (email, password_hash, name)
        VALUES ($1, $2, $3)
        RETURNING id
        """,
        body.email,
        hash_password(body.password),
        body.name,
    )
    return TokenResponse(access_token=create_access_token(user_id))


@router.post("/login", response_model=TokenResponse)
async def login(form: OAuth2PasswordRequestForm = Depends(), conn=Depends(get_db)):
    row = await conn.fetchrow(
        "SELECT id, password_hash FROM users WHERE email = $1", form.username
    )
    if not row or not verify_password(form.password, row["password_hash"]):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return TokenResponse(access_token=create_access_token(row["id"]))


@router.get("/me", response_model=UserResponse)
async def get_me(
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    row = await conn.fetchrow(
        "SELECT id, email, name, gender, birth_date FROM users WHERE id = $1", user_id
    )
    return dict(row)


@router.patch("/me", response_model=UserResponse)
async def update_profile(
    body: UpdateProfileRequest,
    user_id: uuid.UUID = Depends(get_current_user),
    conn=Depends(get_db),
):
    row = await conn.fetchrow(
        """
        UPDATE users
        SET name       = COALESCE($2, name),
            gender     = COALESCE($3, gender),
            birth_date = COALESCE($4, birth_date)
        WHERE id = $1
        RETURNING id, email, name, gender, birth_date
        """,
        user_id,
        body.name,
        body.gender,
        body.birth_date,
    )
    return dict(row)
