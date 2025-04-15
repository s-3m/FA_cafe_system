from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")

    user: str = "postgres_user"
    password: str = "postgres_password"
    host: str = "localhost"
    port: str = "postgres_port"
    name: str = "postgres_db"
    echo: bool = True

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"
