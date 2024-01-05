# app/main.py (App entry point)
'''
from db.session import async_create_tables, async_session
# 一定要导入所有的模型，确保它们被注册到Base.metadata
import models.order  

async def main():
    # 创建数据库表
    await async_create_tables()

    # 启动 web 服务代码，例如使用 uvicorn 或其他

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())   

'''
from app.middleware import token_validator_middleware
from fastapi import FastAPI
from app.api.api_v1.api import api_router

app = FastAPI()

app.middleware("http")(token_validator_middleware)

app.include_router(api_router)

