from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent


class DbSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=BASE_DIR / ".env")

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    host: str = "localhost"
    POSTGRES_PORT: int
    POSTGRES_DB: str
    echo: bool = True

    @property
    def url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.host}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"


print(f"Env file path: {BASE_DIR / '.env'}")
print(f"File exists: {(BASE_DIR / '.env').exists()}")
