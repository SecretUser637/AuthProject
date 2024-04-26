from pydantic import EmailStr,BaseModel, Field
from datetime import date,datetime

class UserBase(BaseModel):
    id: int = Field(None,  example=1)
    email: EmailStr = Field(..., example='help@gmail.com')
    username:str=Field(...,example='nagibator69')
    birthday:date=Field(...,example='01-01-2001')
    email_verify:bool=Field(...)
    created_at:datetime=Field(...,example='01-01-2001 00:00:00')

    class Config:
        orm_mode=True