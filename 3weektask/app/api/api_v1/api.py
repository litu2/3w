#app/api/api_v1/api.py
'''
对API路由进行汇总处理

'''
from fastapi import APIRouter
from app.api.api_v1.endpoints import user,advisor

api_router = APIRouter()

api_router.include_router(user.router,prefix="/user", tags=["用户"])
api_router.include_router(advisor.router,prefix="/advisor", tags=["顾问"])
