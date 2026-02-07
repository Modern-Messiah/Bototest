import os
import tempfile
import pytest
from collections.abc import Generator
from fastapi.testclient import TestClient
from app import database
from app.main import app

@pytest.fixture
def test_db() -> Generator[str, None, None]:
    fd, path = tempfile.mkstemp(suffix=".db")
    os.close(fd)
    original_db_path = database.DB_PATH
    database.DB_PATH = path
    database.init_db()
    yield path
    database.DB_PATH = original_db_path
    os.unlink(path)

@pytest.fixture
def client(test_db: str) -> Generator[TestClient, None, None]:
    with TestClient(app) as test_client:
        yield test_client
