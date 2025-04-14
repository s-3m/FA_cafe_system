from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

from src.config.db_config import DbSettings

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Settings(BaseSettings):
    db: DbSettings = DbSettings()


settings = Settings()
