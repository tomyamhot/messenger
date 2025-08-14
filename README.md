# Мини-мессенджер на FastAPI

Это мой небольшой учебный проект — чат с авторизацией и WebSocket.  
Хотел попробовать FastAPI, асинхронность и работу с базой PostgreSQL в Docker.

---

## Что умеет
- Регистрация пользователей
- Авторизация через JWT (OAuth2)
- Отправка сообщений в реальном времени через WebSocket
- Сохранение истории сообщений в PostgreSQL
- Запуск в Docker + docker-compose

---

## Как запустить

1. Скачайте репозиторий и перейдите в папку проекта:
```bash
git clone https://github.com/username/messenger.git
cd messenger
```

2. Запустите контейнеры:
```bash
docker-compose up --build
```

3. Приложение будет доступно по адресу:
```
http://localhost:8000
```

Документация API (Swagger UI) — тут:
```
http://localhost:8000/docs
```

---

## Как протестировать чат

1. **Зарегистрировать пользователя**
   - POST `/register`
   - JSON:
     ```json
     {
       "username": "testuser",
       "password": "pass"
     }
     ```

2. **Авторизоваться и получить токен**
   - POST `/login`
   - Form-data:
     ```
     username: testuser
     password: pass
     ```
   - В ответ придёт `access_token`.

3. **Подключиться к чату**
   - WebSocket эндпоинт: `ws://localhost:8000/ws/chat`
   - В заголовок нужно передать токен:
     ```
     Authorization: Bearer <токен>
     ```
   - Можно протестировать через Postman или расширение для браузера "WebSocket Client".

---

## Стек технологий
- Python 3.11
- FastAPI
- SQLAlchemy (async)
- PostgreSQL
- Docker + docker-compose
- JWT (python-jose)
- passlib для хэширования паролей

---

## Зачем делал
Хотел сделать простой пример мессенджера, где можно потренироваться с:
- Асинхронными запросами
- WebSocket
- Авторизацией через JWT
- Работой с базой в Docker

---

## Запуск тестов
```bash
pytest
```
