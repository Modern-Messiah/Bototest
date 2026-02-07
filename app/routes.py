from typing import Any
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import RedirectResponse, JSONResponse

from app.database import create_link, get_link_by_code
from app.logger import logger
from app.service import build_short_url, generate_short_code


router = APIRouter()

@router.post("/shorten")
async def shorten_url(request: Request) -> JSONResponse:
    try:
        body = await request.json()
    except Exception:
         raise HTTPException(status_code=422, detail="Invalid JSON")

    original_url = body.get("url")
    if not original_url:
        raise HTTPException(status_code=422, detail="Field 'url' is required")
    
    # Simple validation using str (validation logic from Pydantic HttpUrl is gone, 
    # but we can do basic check or rely on it being a string)
    if not isinstance(original_url, str) or not original_url.startswith(("http://", "https://")):
         raise HTTPException(status_code=422, detail="Invalid URL format")

    short_code = generate_short_code()
    create_link(original_url, short_code)
    short_url = build_short_url(short_code)

    logger.info(f"Shortened URL created: {original_url} -> {short_url}")

    return JSONResponse(content={"short_url": short_url})
