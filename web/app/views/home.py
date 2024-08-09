from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from app import templates

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
@router.get("/home", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request},
    )
