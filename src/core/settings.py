import asyncio
import sys
from functools import cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_PORT: int


class TestSettings(Settings):
    model_config = SettingsConfigDict(env_prefix="TEST_")


@cache
def get_settings() -> Settings:
    if "pytest" in sys.modules:
        return TestSettings()
    return Settings()
