from sqlalchemy import Column,Integer, String,Boolean,Float,Enum,Text,DateTime,func
from app.db.base import Base
from app.db.session import async_engine
import enum

# 订单状态枚举类型定义
class OrderStatus(enum.Enum):
    pending = "pending"
    completed = "completed"
    expired = "expired"

# 订单类型枚举类型定义
class OrderType(enum.Enum):
    text_consultation = "text"
    video_consultation = "video"
    voice_consultation = "voice"
    livetestchat_consultation = "livetestchat_consultation"

class Order(Base):
    __tablename__ = "orders"

    # 订单id
    order_id = Column(Integer, primary_key=True)
    # 用户id
    user_id = Column(Integer)
    # 顾问id
    advisor_id = Column(Integer)
    #备注
    notes = Column(String(256))
    # 问题内容字段，用于存放文本或媒体文件引用
    question_content = Column(Text(), nullable=True)
    # 问题类型字段，标识问题是文本、语音还是视频
    order_type = Column(Enum(OrderType), nullable=False)
    # 订单金额
    amount = Column(Float, nullable=False)
    # 订单状态
    status = Column(Enum(OrderStatus), default=OrderStatus.pending, nullable=False)
    # 是否加急
    is_urgent = Column(Boolean, default=False, nullable=False) 
    # 订单内容
    response = Column(Text)
    # 订单创建时间
    created_at = Column(DateTime, default=func.now())  
    # 订单更新时间
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



