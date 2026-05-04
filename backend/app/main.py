from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import create_pool, close_pool
from app.auth.router import router as auth_router
from app.themes.router import router as themes_router
from app.hypotheses.router import router as hypotheses_router
from app.dashboard.router import router as dashboard_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_pool()
    yield
    await close_pool()


app = FastAPI(
    title="МедДневник API",
    version="1.0.0",
    description="Backend for МедДневник mobile app — problem-oriented medical diary.",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

PREFIX = "/api/v1"

app.include_router(auth_router,        prefix=PREFIX)
app.include_router(themes_router,      prefix=PREFIX)
app.include_router(hypotheses_router,  prefix=PREFIX)
app.include_router(dashboard_router,   prefix=PREFIX)


@app.get("/health", tags=["system"])
async def health():
    return {"status": "ok"}
