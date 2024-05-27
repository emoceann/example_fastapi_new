import pytest

from fastapi import FastAPI
from httpx import AsyncClient
from sqlalchemy import text, table, column
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine, async_sessionmaker

from src.core.settings import get_settings
from src.server.app import get_app
from tests.utils import generate_data

settings = get_settings()

@pytest.fixture(scope="session")
async def get_db_session():
    engine: AsyncEngine = create_async_engine(
        url=f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@{settings.POSTGRES_HOST}/{settings.POSTGRES_DB}",
        echo=True,
        echo_pool=True
    )
    session_maker = async_sessionmaker(bind=engine, autocommit=False, autoflush=False)
    async with session_maker() as session:
        yield session


@pytest.fixture(scope="session")
async def prepare_db(get_db_session):
    await get_db_session.execute(text(
        "CREATE TABLE IF NOT EXISTS data_first (id INT PRIMARY KEY,name VARCHAR(255)); "
    ))
    await get_db_session.execute(text(
        "CREATE TABLE IF NOT EXISTS data_second (id INT PRIMARY KEY,name VARCHAR(255));"
    ))
    await get_db_session.execute(text(
        "CREATE TABLE IF NOT EXISTS data_third (id INT PRIMARY KEY,name VARCHAR(255));"
    ))
    data = generate_data(1, 11)
    data.extend(generate_data(31, 41))
    await get_db_session.execute(
        table("data_first", column("id"), column("name")).insert(), data
    )
    data = generate_data(11, 21)
    data.extend(generate_data(41, 51))
    await get_db_session.execute(
        table("data_second", column("id"), column("name")).insert(), data
    )
    data = generate_data(21, 31)
    data.extend(generate_data(51, 61))
    await get_db_session.execute(
        table("data_third", column("id"), column("name")).insert(), data
    )
    await get_db_session.commit()
    yield
    await get_db_session.execute(
        text("DROP TABLE data_first")
    )
    await get_db_session.execute(
        text("DROP TABLE data_second")
    )
    await get_db_session.execute(
        text("DROP TABLE data_third")
    )
    await get_db_session.commit()


@pytest.fixture(scope="session")
def app() -> FastAPI:
    return get_app()

@pytest.fixture(scope="session")
async def client(app) -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as client:
        yield client
