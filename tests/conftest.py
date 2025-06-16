import os
from pathlib import Path

from fastapi.testclient import TestClient
import pytest
import pytest_asyncio
from mixer.backend.sqlalchemy import Mixer as _mixer
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import sessionmaker



os.environ["DATABASE_URL"] = "sqlite+aiosqlite:///./test.db"

from app.core.db import Base
from app.main import app
from app.core.db import get_async_session


BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

pytest_plugins = [
    'tests.fixtures.user',
    'tests.fixtures.data',
]


TEST_DB = BASE_DIR / 'test.db'
SQLALCHEMY_DATABASE_URL = f'sqlite+aiosqlite:///{str(TEST_DB)}'

engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommit=False,
)


async def override_db():
    async with TestingSessionLocal() as session:
        yield session


@pytest_asyncio.fixture(autouse=True, scope="function")
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture
def client():
    with TestClient(app) as c:
        yield c


@pytest.mark.asyncio
async def test_some_endpoint(client):
    response = await client.get("/some-endpoint")
    assert response.status_code == 200


@pytest.fixture
def mixer():
    from sqlalchemy import create_engine

    sync_engine = create_engine(f'sqlite:///{str(TEST_DB)}')
    SyncSession = sessionmaker(bind=sync_engine)
    return _mixer(session=SyncSession(), commit=True)
