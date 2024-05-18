from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import pyd
from datetime import date
from myemail import send_email_message
import random
import string
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from auth import auth


def randomword(length):
    letters = string.ascii_lowercase+string.digits
    return ''.join(random.choice(letters) for i in range(length))


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.post('/reg', response_model=pyd.UserBase)
async def reg_user(user_input: pyd.UserCreate, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.email == user_input.email).first()
    if user_db:
        raise HTTPException(400, 'Email занят')
    user_db = models.User()

    user_db.email = user_input.email
    user_db.hash_pwd = auth.get_password_hash(user_input.pwd)
    user_db.username = user_input.username
    if user_input.birthday >= date.today():
        raise HTTPException(400, 'Ты еще не родился')
    user_db.birthday = user_input.birthday
    db.add(user_db)
    db.commit()
    email_verify_token = randomword(25)
    email_verify_token += str(user_db.id)
    user_db.email_verify_code = email_verify_token
    db.commit()

    # send_email_message(user_db.email, 'Проверочное письмо 1',
    #    f'<h1>Проверка</h1><a href="http://127.0.0.1:8000/verify/?code={email_verify_token}">Подтвердить почту</a>')

    return user_db


@app.get('/verify')
async def verify_email(code: str, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.email_verify_code == code).first()
    if not user_db:
        raise HTTPException(400, 'Неверный код')
    user_db.email_verify = True
    user_db.email_verify_code = None
    db.commit()
    return RedirectResponse('http://localhost:5173/')


@app.post('/login', response_model=pyd.JWTToken)
async def user_login(cred: pyd.Credentials, db: Session = Depends(get_db)):
    user_db = db.query(models.User).filter(
        models.User.email == cred.email).first()
    if not user_db:
        raise HTTPException(404, 'Не найден')
    if not user_db.email_verify:
        raise HTTPException(400, 'Почта')
    if not auth.verify_password(cred.pwd, user_db.hash_pwd):
        raise HTTPException(403, 'не верный логин или пароль')

    return auth.encode_token(user_db.id)


@app.get('/secr')
async def sectr(user=Depends(auth.auth_wrapper)):
    return randomword(30)
