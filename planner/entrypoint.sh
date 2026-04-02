#!/bin/sh

echo "⏳ Ждём базу данных..."

while ! nc -z db 5432; do
  sleep 1
done

echo "✅ База данных готова!"

echo "📦 Применяем миграции..."
python manage.py migrate

#echo "👤 Создаём суперпользователя (если нет)..."
#python manage.py createsuperuser --noinput || true

echo "🚀 Запуск сервера..."
python manage.py runserver 0.0.0.0:8000