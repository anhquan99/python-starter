from functools import lru_cache
from fastapi import FastAPI, Depends
from typing_extensions import Annotated
import os
from .config import Settings



app = FastAPI()

@lru_cache
def get_settings():
    return Settings()

@app.get("/info")
async def info(settings: Annotated[Settings, Depends(get_settings)]):
    return {
        "app_name": settings.app_name,
        "build_name": settings.build_name,
    }

# @app.get("/settings")
# def get_settings(settings: Annotated[Settings, Depends(get_settings)]):

#     return {"app_name": settings.app_name, "build_name": settings.build_name}