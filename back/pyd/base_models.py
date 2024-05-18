from pydantic import EmailStr, BaseModel, Field
from datetime import date, datetime


class UserBase(BaseModel):
    id: int = Field(None,  example=1)
    email: EmailStr = Field(..., example='help@gmail.com')
    username: str = Field(..., example='nagibator69')
    birthday: date = Field(..., example='2001-01-01')
    email_verify: bool = Field(...)
    created_at: datetime = Field(..., example='2001-01-01 00:00:00')

    class Config:
        orm_mode = True


class JWTToken(BaseModel):
    exp: datetime = Field(..., example='2001-01-01 00:00:00')
    token: str = Field(..., example='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTYwMDg5NzUsImlhdCI6MTcxNjAwNzE3NSwidXNlcl9pZCI6MX0.o-36LfTtQ1ksQR4o3T_FApzXD1ss-56LsqytsLvpKd4')
