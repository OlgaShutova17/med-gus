import uuid
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.config import settings
from app.database import get_pool

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


async def get_db():
    """Yield a single asyncpg connection from the pool."""
    pool = get_pool()
    async with pool.acquire() as conn:
        yield conn


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    conn=Depends(get_db),
) -> uuid.UUID:
    """Decode JWT and return user UUID. Raises 401 on any error."""
    credentials_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=["HS256"])
        user_id: str | None = payload.get("sub")
        if user_id is None:
            raise credentials_exc
    except JWTError:
        raise credentials_exc

    row = await conn.fetchrow("SELECT id FROM users WHERE id = $1", uuid.UUID(user_id))
    if row is None:
        raise credentials_exc

    return uuid.UUID(user_id)
