from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request

from .views import home, coffee_types, shops_nearby

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/resources/static"), name="static")

app.include_router(home.router)
app.include_router(coffee_types.router)
app.include_router(shops_nearby.router)
