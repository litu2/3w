#app/models/advisor.py
'''

SQLAlchemy
定义ORM映射类user


'''
from sqlalchemy import Column, Integer, String, Boolean, Float,Enum
from app.db.base import Base
from app.db.session import async_engine
import enum

#接单状态枚举类型定义
class Workstatus(enum.Enum):
    online_free = "online_free"
    online_busy = "online_busy"
    offline = "offline"
    online = "online"


class Advisor(Base):
    __tablename__ = 'advisor'  # 表名

    id = Column(Integer, primary_key=True)
    #顾问名字
    name = Column(String(256), nullable=True)
    #顾问手机号
    mobile = Column(String(256), unique=True, nullable=False)
    #顾问密码
    hashed_password = Column(String(256), nullable=False)
    #顾问工作经验
    experience=Column(String(256), nullable=True)
    #顾问自我简介
    bio = Column(String(256), nullable=True)
    #顾问自我繁介
    about = Column(String(512), nullable=True)
    #顾问金币
    coin = Column(Float, default=0.0)
    #顾问接单状态
    workstatus = Column(Enum(Workstatus), nullable=False, default=Workstatus.offline)
    #总订单数
    readings = Column(Integer, default=0)
    #完成订单数
    complete = Column(Integer, default=0)
    #评分
    rating = Column(Float, default=0)
    #评论数
    commentCount = Column(Integer, default=0)
    #服务设置
    textReadingStatus = Column(Boolean, nullable=True,default = True)
    textReadingPrice = Column(Float, nullable=True)  
    audioReadingStatus = Column(Boolean, nullable=True,default = True)
    audioReadingPrice = Column(Float, nullable=True)
    videoReadingStatus = Column(Boolean, nullable=True,default = True)
    videoReadingPrice = Column(Float, nullable=True)
    liveTextChatStatus = Column(Boolean, nullable=True,default = True)
    liveTextChatPrice = Column(Float, nullable=True)
