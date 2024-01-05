#app/schemas/advisor.py
'''
advisor的Pydantic校验模型
各种校验数据模型
'''


from pydantic import BaseModel, Field
from pydantic.types import constr
from typing import Optional
from datetime import date
import enum

# 接单状态枚举类，与SQLAlchemy模型保持一致
class Workstatus(str, enum.Enum):
    online_free = "online_free"
    online_busy = "online_busy"
    offline = "offline"
    online = "online"

# 顾问基础模型
class AdvisorBase(BaseModel):
    name: Optional[str] = Field(None, example="John Doe")
    experience: str = Field(..., example="5 years of experience")
    bio: Optional[str] = Field(None, example="A short bio here")
    about: Optional[str] = Field(None, example="More details about the advisor")
    coin: float = Field(0.0, example=100.0)
    workstatus: Optional[Workstatus] = Field(None, example="online_free")
    readings: int = Field(0, example=10)
    complete: int = Field(0, example=5)
    rating: float = Field(0.0, example=4.5)
    commentCount: int = Field(0, example=8)
    textReadingStatus: Optional[bool] = Field(True)
    textReadingPrice: Optional[float] = Field(None, example=10.0)
    audioReadingStatus: Optional[bool] = Field(True)
    audioReadingPrice: Optional[float] = Field(None, example=20.0)
    videoReadingStatus: Optional[bool] = Field(True)
    videoReadingPrice: Optional[float] = Field(None, example=30.0)
    liveTextChatStatus: Optional[bool] = Field(True)
    liveTextChatPrice: Optional[float] = Field(None, example=40.0)

    class Config:
        use_enum_values = True  # 使枚举字段返回值

class AdvisorOut(BaseModel):
    id: int
    name: Optional[str] = Field(None)
    bio: Optional[str] = Field(None)
    workstatus: Optional[Workstatus] = Field(None)
    experience: Optional[str] = Field(None)
    rating: Optional[float] = Field(None)
    about: Optional[str] = Field(None)

    readings: Optional[int] = Field()
    complete: Optional[int] = Field()
    commentCount: Optional[int] = Field()

    coin: Optional[float] = Field()
    class Config:
        from_attributes = True
        use_enum_values = True  # 使枚举字段返回值




# 顾问注册模型
class AdvisorCreate(BaseModel):
    mobile: str = Field(..., example="13812345678")
    password: str = Field(..., example="supersecretpassword")


# 顾问登录模型
class AdvisorLogin(BaseModel):
    mobile: str = Field(..., example="13812345678")
    password: str = Field(..., example="supersecretpassword")


# 顾问修改信息模型，继承自顾问基础模型
class AdvisorUpdate(AdvisorBase):
    name: Optional[str] = Field(None, example="John Doe")
    experience: str = Field(..., example="5 years of experience")
    bio: Optional[str] = Field(None, example="A short bio here")
    about: Optional[str] = Field(None, example="More details about the advisor")

# 顾问修改服务状态模型
class AdvisorServiceSetting(BaseModel):
    textReadingStatus: Optional[bool] = Field(True)
    textReadingPrice: Optional[float] = Field(None, example=10.0)
    audioReadingStatus: Optional[bool] = Field(True)
    audioReadingPrice: Optional[float] = Field(None, example=20.0)
    videoReadingStatus: Optional[bool] = Field(True)
    videoReadingPrice: Optional[float] = Field(None, example=30.0)
    liveTextChatStatus: Optional[bool] = Field(True)
    liveTextChatPrice: Optional[float] = Field(None, example=40.0)

#顾问修改接单状态模型
class AdvisorUpdateWorkstatus(BaseModel):
    workstatus: Optional[Workstatus] = Field(None, example="online_free")

class AdvisorList(BaseModel):
    id: int
    name: Optional[str] = Field(None, example="John Doe")
    bio: Optional[str] = Field(None, example="A short bio here")
class AdvisorDetailed(BaseModel):
    id: int
    name: Optional[str] = Field(None, example="John Doe")
    bio: Optional[str] = Field(None, example="A short bio here")
    experience: str = Field(..., example="5 years of experience")
    about: Optional[str] = Field(None, example="More details about the advisor")
    textReadingStatus: Optional[bool] = Field(True)
    textReadingPrice: Optional[float] = Field(None, example=10.0)
    audioReadingStatus: Optional[bool] = Field(True)
    audioReadingPrice: Optional[float] = Field(None, example=20.0)
    videoReadingStatus: Optional[bool] = Field(True)
    videoReadingPrice: Optional[float] = Field(None, example=30.0)
    liveTextChatStatus: Optional[bool] = Field(True)
    liveTextChatPrice: Optional[float] = Field(None, example=40.0)

# 顾问返回信息模型，继承自顾问基础模型
class Advisor(AdvisorBase):
    mobile: str = Field(..., example="13812345678")
    password: str = Field(..., example="supersecretpassword")
