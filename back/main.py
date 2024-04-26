from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models
import pyd
from datetime import date
from myemail import send_email_message

app = FastAPI()

@app.post('/reg',response_model=pyd.UserBase)
async def reg_user(user_input:pyd.UserCreate,db: Session = Depends(get_db)):
    user_db=db.query(models.User).filter(models.User.email==user_input.email).first()
    if user_db:
        raise HTTPException(400, 'Email занят')
    user_db=models.User()

    user_db.email=user_input.email
    user_db.hash_pwd=user_input.pwd
    user_db.username=user_input.username
    if user_input.birthday>=date.today():
        raise HTTPException(400, 'Ты еще не родился')
    user_db.birthday=user_input.birthday
    db.add(user_db)
    db.commit()

    send_email_message(user_db.email,'Проверка почты','Привет мир, как ты?')

    return user_db