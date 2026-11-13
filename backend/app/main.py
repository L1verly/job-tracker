from fastapi import FastAPI
from .core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
)


@app.get("/health")
async def root():
    return {"status": "OK"}
