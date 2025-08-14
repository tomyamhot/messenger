import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        resp = await ac.post("/register", json={"username": "testuser", "password": "pass"})
        assert resp.status_code == 200

        resp = await ac.post("/login", data={"username": "testuser", "password": "pass"})
        assert resp.status_code == 200
        assert "access_token" in resp.json()
