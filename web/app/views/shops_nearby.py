from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from app import templates

router = APIRouter()

@router.get("/shops-nearby", response_class=HTMLResponse)
def get_shops_nearby(request: Request):
    return templates.TemplateResponse(
        "shops_nearby.html", {"request": request},
    )
