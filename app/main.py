from contextlib import asynccontextmanager
from typing import AsyncGenerator
from fastapi import FastAPI
from app.database import init_db
from app.logger import logger
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    logger.info("Starting URL Shortener application")
    init_db()
    yield
    logger.info("Shutting down URL Shortener application")


app = FastAPI(
    title="URL Shortener",
    description="Simple URL shortening service",
    version="0.1.0",
    lifespan=lifespan,
)

app.include_router(router)
