from functools import lru_cache
from pathlib import Path

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=ROOT_DIR / ".env",
        extra="ignore",
    )
    PROJECT_NAME: str = "Job Tracker"
    DATABASE_URL: PostgresDsn


@lru_cache
def get_settings() -> Settings:
    return Settings()
