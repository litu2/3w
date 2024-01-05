# middleware.py
from fastapi import Request, HTTPException
from starlette.responses import PlainTextResponse
from starlette.status import HTTP_401_UNAUTHORIZED

'''
async def token_validator_middleware(request: Request, call_next):
    # 不需要token验证的路径列表
    paths_to_exclude = ["/openapi.json","/","/docs","/user/login", "/user/register", "/advisor/login", "/advisor/register"]

    if request.url.path not in paths_to_exclude:
        token = request.headers.get("Authorization")
        expected_token = "mysecrettoken"
        if not token or token != f"Bearer {expected_token}":
            return PlainTextResponse("Invalid or missing token", status_code=HTTP_401_UNAUTHORIZED)

    response = await call_next(request)
    return response
'''

async def token_validator_middleware(request: Request, call_next):
    paths_to_exclude = ["/docs", "/openapi.json", "/user/login", "/user/register", "/advisor/login", "/advisor/register"]

    #print("Request path:", request.url.path)
    # 如果路径以排除项之一开头，则跳过token验证
    if any(request.url.path.startswith(path) for path in paths_to_exclude):
        response = await call_next(request)
        return response
    # 检查请求中是否包含Token
    authorization: str = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        return PlainTextResponse("Unauthorized", status_code=HTTP_401_UNAUTHORIZED)


    response = await call_next(request)
    return response
    
