from functools import lru_cache

from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )
    PROJECT_NAME: str = "Job Tracker"
    DATABASE_URL: PostgresDsn


@lru_cache
def get_settings() -> Settings:
    return Settings()
