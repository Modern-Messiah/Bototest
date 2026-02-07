import sqlite3
from contextlib import contextmanager
from datetime import datetime, timezone
from typing import Generator
from app.config import DATABASE_PATH
from app.logger import logger


DB_PATH = DATABASE_PATH

@contextmanager
def get_connection() -> Generator[sqlite3.Connection, None, None]:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db() -> None:
    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT NOT NULL UNIQUE,
                created_at TEXT NOT NULL
            )
        """)
        conn.execute("CREATE INDEX IF NOT EXISTS idx_short_code ON links(short_code)")
        conn.commit()
    logger.info("Database initialized")
