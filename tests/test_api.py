from fastapi.testclient import TestClient

class TestShortenEndpoint:

    def test_shorten_valid_url(self, client: TestClient) -> None:
        response = client.post(
            "/shorten",
            json={"url": "https://example.com/very/long/path"},
        )

        assert response.status_code == 200
        data = response.json()
        assert "short_url" in data
        assert data["short_url"].startswith("http://localhost:8000/")

    def test_shorten_invalid_url(self, client: TestClient) -> None:
        response = client.post(
            "/shorten",
            json={"url": "not-a-valid-url"},
        )

        assert response.status_code == 422

    def test_shorten_missing_url(self, client: TestClient) -> None:
        response = client.post(
            "/shorten",
            json={},
        )

        assert response.status_code == 422


class TestRedirectEndpoint:

    def test_redirect_valid_code(self, client: TestClient) -> None:
        create_response = client.post(
            "/shorten",
            json={"url": "https://example.com"},
        )
        short_url = create_response.json()["short_url"]
        code = short_url.split("/")[-1]
        response = client.get(f"/{code}", follow_redirects=False)
        assert response.status_code == 307
        assert response.headers["location"] == "https://example.com"

    def test_redirect_nonexistent_code(self, client: TestClient) -> None:
        response = client.get("/nonexistent123")
        assert response.status_code == 404
        assert "not found" in response.json()["detail"].lower()
