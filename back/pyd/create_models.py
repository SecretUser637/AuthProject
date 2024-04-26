from pydantic import EmailStr,BaseModel, Field
from datetime import date,datetime


class UserCreate(BaseModel):
    email: EmailStr = Field(..., example='help@gmail.com')
    username:str=Field(...,max_length=255,min_length=3,example='nagibator69')
    pwd:str=Field(...,max_length=255,min_length=6,example='123456')
    birthday:date=Field(...,example='01-01-2001')
