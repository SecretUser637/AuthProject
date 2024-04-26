from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from database import get_db
import models


app = FastAPI()

@app.post('/reg')
async def reg_user(db: Session = Depends(get_db)):
    return {'mes':1}