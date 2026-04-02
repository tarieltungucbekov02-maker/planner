FROM python:3.13-slim

WORKDIR /app

# Устанавливаем системные зависимости + netcat
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Копируем весь проект
COPY . .

# Точка входа
ENTRYPOINT ["/entrypoint.sh"]

# Запуск сервера (как fallback, если entrypoint не переопределяет)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]