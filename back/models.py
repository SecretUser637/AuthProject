from sqlalchemy import TIMESTAMP,Date,Numeric, Table, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), nullable=False, unique=True)
    hash_pwd=Column(String(255), nullable=False)
    username=Column(String(255), nullable=False)
    birthday=Column(Date(),nullable=False)
    email_verify=Column(Boolean(),nullable=False,
                        default=False)
    email_verify_code=Column(String(255), nullable=True, unique=True)
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())