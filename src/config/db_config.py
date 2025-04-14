from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")

    postgres_user: str = "postgres_user"
    postgres_password: str = "postgres_password"
    POSTGRES_HOST: str = "localhost"
    postgres_port: str = "postgres_port"
    postgres_db: str = "postgres_db"
    db_echo: bool = True


    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.POSTGRES_HOST}:{self.postgres_port}/{self.postgres_db}"
