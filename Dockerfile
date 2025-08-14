FROM python:3.11-slim

WORKDIR /code

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y gcc libpq-dev build-essential

# Обновляем pip
RUN pip install --upgrade pip

# Копируем только requirements.txt для кеша зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальной код
COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
