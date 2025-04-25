from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


# Init app
app = FastAPI()


# Init static
app.mount("/static", StaticFiles(directory="static"), name="static")


# Init routes
from .routes import photo_router, plant_router, frontend_router

app.include_router(plant_router)
app.include_router(photo_router)
app.include_router(frontend_router)
