# URL Shortener

Сервис для сокращения ссылок.

## Запуск

```bash
python -m venv venv
source venv/bin/activate
pip install -e ".[dev]"
uvicorn app.main:app --reload
```

## Тесты

```bash
pytest -v
```

## API

**POST /shorten**
```bash
curl -X POST http://localhost:8000/shorten -H "Content-Type: application/json" -d '{"url": "https://example.com"}'
# {"short_url": "http://localhost:8000/abc123"}
```

**GET /{code}** — редирект на оригинальный URL

## Допущения

- Формат: `{"url": "..."}` → `{"short_url": "..."}`
- Редирект: HTTP 307
- Валидация URL: Ручная проверка (http/https)
- Код не найден: HTTP 404
