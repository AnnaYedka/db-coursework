from pydantic_settings import BaseSettings, SettingsConfigDict
import os


class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg://postgres:postgres@localhost:5432/sa"
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret-key"


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DATABASE_URL_asyncpg(self):
        "Return DataSourceName(DSN) for PostgreSQL async connection."
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    @property
    def DATABASE_URL_psycopg(self):
        "Return DataSourceName(DSN) for PostgreSQL sync connection."
        return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=".env")


# settings = Settings()  # type: ignore
