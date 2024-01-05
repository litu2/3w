#app/db/session.py
'''
SQLAlchemy
建造异步数据库引擎，为数据库操作提供异步sesion

'''
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession ,create_async_engine
from app.db.base import Base

DATABASE_URL = "mysql+aiomysql://work:work2023@localhost/dbxu"

async_engine = create_async_engine(DATABASE_URL,echo=True)

async_session = sessionmaker(async_engine, class_=AsyncSession)


#创建mysql表
async def async_create_tables():
    # 创建异步会话
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


