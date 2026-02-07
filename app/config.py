import os

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
DATABASE_PATH = os.getenv("DATABASE_PATH", "urls.db")
SHORT_CODE_LENGTH = int(os.getenv("SHORT_CODE_LENGTH", "6"))
