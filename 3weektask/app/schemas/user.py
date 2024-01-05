#app/schemas/user.py
'''
user的Pydantic校验模型
各种校验数据模型

'''


from pydantic import BaseModel, Field
from pydantic.types import constr
from typing import Optional
from datetime import date
import enum


# 性别枚举类，与SQLAlchemy模型保持一致
class Gender(str, enum.Enum):
    male = "male"
    female = "female"
    other = "other"

# 用户基础模型
class UserBase(BaseModel):
    name: Optional[str] = Field(None, example="John Doe")
    birth: Optional[date] = Field(None, example="1980-01-01")
    gender: Optional[Gender] = Field(None, example="male")
    bio: Optional[str] = Field(None, example="A short bio here")
    about: Optional[str] = Field(None, example="More details about the user")

    class Config:
        use_enum_values = True  # 使枚举字段返回值

# 用户注册模型
class UserCreate(UserBase):
    mobile:  str  = Field(..., example="13812345678")
    password: str = Field(..., example="supersecretpassword")

# 用户注册输出模型
class UserCreateOut(UserCreate):
    class Config:
        exclude_unset = True
    pass




# 用户登录模型
class UserLogin(BaseModel):
    mobile: str = Field(..., example="13812345678")
    password: str = Field(..., example="supersecretpassword")

# 用户修改信息模型，继承自用户基础模型
class UserUpdate(UserBase):
    pass



class User(UserBase):
    mobile:  str = Field(..., example="13812345678")
    password: str = Field(..., example="supersecretpassword")

'''
# 用户展示模型
class User(UserBase):
    id: int = Field(..., example=1)
    coin: float = Field(default=0.0, example=100.0)

    class Config(UserBase.Config):
        orm_mode = True  # 允许模型与ORM模型匹配    
'''


