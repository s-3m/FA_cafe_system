from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

from src.config.db_config import DbSettings

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")

    db: DbSettings = DbSettings()


settings = Settings()
