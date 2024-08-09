from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from app import templates

router = APIRouter()

@router.get("/coffee-types", response_class=HTMLResponse)
async def get_coffee_types(request: Request):
    return templates.TemplateResponse(
        "coffee_types.html", {"request": request},
    )
