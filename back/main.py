from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import get_db
import models
import pyd

app = FastAPI()

@app.post('/reg',response_model=pyd.UserBase)
async def reg_user(user_input:pyd.UserCreate,db: Session = Depends(get_db)):
    return {'mes':1}