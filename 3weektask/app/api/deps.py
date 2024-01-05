#app/api/deps.py
'''
实现一些依赖项函数，用于路由层的依赖注入

'''


from typing import AsyncGenerator
from app.db.session import async_session



#用于依赖注入AsyncSession
async def get_async_db() ->AsyncGenerator:
    async with async_session() as asyncsession:
        yield asyncsession




