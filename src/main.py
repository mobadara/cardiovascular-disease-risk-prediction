from fastapi import FastAPI

from .models.predictions import router as predictions_router

app = FastAPI()

app.include_router(predictions_router, prefix="/api")