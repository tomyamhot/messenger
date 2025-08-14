from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from . import models, schemas, utils, auth, database, chat
from fastapi.security import OAuth2PasswordRequestForm


app = FastAPI()

from fastapi.responses import HTMLResponse

@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head>
            <title>Messenger API</title>
        </head>
        <body style="font-family: Arial; text-align: center; padding-top: 50px;">
            <h1>Messenger API</h1>
            <p>тест апи.</p>

            <h2>Регистрация</h2>
            <form action="/register" method="post" onsubmit="event.preventDefault(); registerUser();">
                <input type="text" id="reg_username" placeholder="Username" required><br><br>
                <input type="password" id="reg_password" placeholder="Password" required><br><br>
                <button type="submit">Зарегистрироваться</button>
            </form>

            <h2>Логин</h2>
            <form action="/login" method="post" onsubmit="event.preventDefault(); loginUser();">
                <input type="text" id="login_username" placeholder="Username" required><br><br>
                <input type="password" id="login_password" placeholder="Password" required><br><br>
                <button type="submit">Войти</button>
            </form>

            <script>
                async function registerUser() {
                    const username = document.getElementById("reg_username").value;
                    const password = document.getElementById("reg_password").value;
                    const res = await fetch("/register", {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: JSON.stringify({ username, password })
                    });
                    alert(await res.text());
                }

                async function loginUser() {
                    const formData = new FormData();
                    formData.append("username", document.getElementById("login_username").value);
                    formData.append("password", document.getElementById("login_password").value);
                    const res = await fetch("/login", { method: "POST", body: formData });
                    alert(await res.text());
                }
            </script>
        </body>
    </html>
    """


@app.on_event("startup")
async def startup():
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

@app.post("/register", response_model=schemas.UserOut)
async def register(user: schemas.UserCreate, db: AsyncSession = Depends(database.get_db)):
    db_user = models.User(username=user.username, hashed_password=utils.hash_password(user.password))
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@app.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: AsyncSession = Depends(database.get_db)):
    user = await auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = auth.create_access_token({"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

app.include_router(chat.router)
