# Weather Query Web Application 🌦️

Простое веб-приложение на Flask для получения текущей погоды по названию города и сохранения истории запросов в PostgreSQL.

## 📦 Стек технологий

- Python
- Flask
- PostgreSQL
- SQLAlchemy
- OpenWeatherMap API
- HTML (Jinja2)

## 🚀 Установка и запуск

### Вариант 1: без Docker

1. Установи PostgreSQL и создай БД:
```sql
CREATE DATABASE weather_db;
```

2. Установи зависимости:
```bash
pip install -r requirements.txt
```

3. Запусти приложение:
```bash
python app.py
```

### Вариант 2: через Docker

```bash
docker-compose up --build
```

Приложение будет доступно на [http://localhost:5000](http://localhost:5000)

## 🧪 Тестирование

```bash
python test_app.py
```
