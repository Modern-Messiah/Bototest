import secrets
import string
from app.config import BASE_URL, SHORT_CODE_LENGTH
from app.database import code_exists


def generate_short_code(length: int | None = None) -> str:
    if length is None:
        length = SHORT_CODE_LENGTH
    alphabet = string.ascii_letters + string.digits
    while True:
        code = "".join(secrets.choice(alphabet) for _ in range(length))
        if not code_exists(code):
            return code

def build_short_url(short_code: str) -> str:
    return f"{BASE_URL.rstrip('/')}/{short_code}"
