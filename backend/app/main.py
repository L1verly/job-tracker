from fastapi import FastAPI

from app.core.config import get_settings

settings = get_settings()

app = FastAPI(title=settings.PROJECT_NAME)


@app.get("/health")
def health():
    return {"status": "OK"}
