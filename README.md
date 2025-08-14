# Мини-мессенджер на FastAPI

Это мой небольшой  проект — чат с авторизацией и WebSocket.  
пробуем фаст апишку, асинхронность и работу с базой постгре в Docker.

---

## Что умеет
- Регистрация пользователей
- Авторизация через JWT (OAuth2)
- Отправка сообщений в реальном времени через WebSocket
- Сохранение истории сообщений в PostgreSQL
- Запуск в Docker + docker-compose

---

## Запуск

1. Скачать репозиторий и перейти в папку проекта:
```bash
git clone https://github.com/tomyamhoot/messenger_project_docker_fixed.git
cd messenger_project_docker_fixed/messenger
```

2. Запустить контейнер:
```bash
docker-compose up --build
```

3. адрес:
```
http://localhost:8000
```

документация API сваггер — тут:
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
   - тест через постмен

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
Хотел сделать простой пример мессенджера, и потренировался
- Асинхронными запросами
- WebSocket
- Авторизацией через JWT
- Работой с базой в Docker

---

## Запуск тестов
```bash
pytest
```

