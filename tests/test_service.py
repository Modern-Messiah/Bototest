from app.service import build_short_url, generate_short_code


class TestGenerateShortCode:

    def test_code_length(self, test_db: str) -> None:
        code = generate_short_code()
        assert len(code) == 6

    def test_code_custom_length(self, test_db: str) -> None:
        code = generate_short_code(length=10)
        assert len(code) == 10

    def test_code_alphanumeric(self, test_db: str) -> None:
        code = generate_short_code()
        assert code.isalnum()

    def test_codes_unique(self, test_db: str) -> None:
        codes = [generate_short_code() for _ in range(100)]
        assert len(codes) == len(set(codes))

class TestBuildShortUrl:
    def test_build_short_url(self) -> None:
        url = build_short_url("abc123")
        assert url == "http://localhost:8000/abc123"
