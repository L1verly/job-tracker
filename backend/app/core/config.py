
from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file="../.env"
    )
    PROJECT_NAME: str = "Job Tracker"
    DATABASE_URL: PostgresDsn


settings = Settings()
