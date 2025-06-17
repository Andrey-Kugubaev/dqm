#!/bin/sh
set -e

# Применяем миграции
alembic upgrade head

# Запускаем скрипт заполнения базы
python /app/seed_data.py

# Запускаем uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
