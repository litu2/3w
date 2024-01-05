#app/models/user.py
'''

SQLAlchemy
定义ORM映射类user


'''
from sqlalchemy import Column, Integer, String, Date, Enum, Float
from app.db.base import Base
from app.db.session import async_engine
import enum

# 性别枚举类型定义
class Gender(enum.Enum):
    male = "male"
    female = "female"
    other = "other"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(256), index=True)
    mobile = Column(String(256), unique=True, index=True, nullable=False)
    hashed_password = Column(String(256), nullable=False)
    birth = Column(Date, nullable=True)
    gender = Column(Enum(Gender), nullable=True)
    bio = Column(String(512), nullable=True)
    about = Column(String(512), nullable=True)
    coin = Column(Float, default=0.0)


    
    

