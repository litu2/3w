#api/api_v1/endpoint/user.py
'''
和用户有关的API
'''
from fastapi import APIRouter, Depends, HTTPException,status,Query,Path
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import Response
from datetime import timedelta
from app.crud.crud_user import get_user_by_mobile, create_user,update_user
from app.crud.crud_advisor import get_advisors_after_cursor,get_paged_advisors,get_advisor_detail
from app.schemas.user import UserCreate,UserLogin,UserUpdate,UserCreateOut
from app.schemas.advisor import AdvisorList,AdvisorDetailed
from app.api.deps import get_async_db
from app.core.security import verify_password,create_access_token,get_current_user
from typing import List


router = APIRouter()

#用户注册接口
@router.post("/register",description="用户注册")
async def user_register(user_in: UserCreate, db: AsyncSession = Depends(get_async_db)):
    # 检查用户是否已经存在
    user = await get_user_by_mobile(db, mobile=user_in.mobile)
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Mobile already registered."
        )
    
    # 返回数据处理
    
    user_out = await create_user(db=db, user=user_in)  
    return user_out


# 用户登录接口
@router.post("/login",description="用户登录")
async def user_login(user_in: UserLogin, db: AsyncSession = Depends(get_async_db)):
    # 根据用户提供的信息查询用户
    user = await get_user_by_mobile(db, mobile=user_in.mobile)

    # 检查用户是否存在，并验证密码
    if not user or not verify_password(user_in.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid mobile or password"
        )

    # 创建访问令牌
    access_token = create_access_token(subject=user.id, expires_delta=timedelta(minutes=60*24*7))

    # 创建响应对象，设置响应头
    response = Response()
    response.headers["Authorization"] = f"Bearer {access_token}"
    response.headers["token_type"] = "bearer"

    # 返回响应
    return response


# 用户修改个人信息接口
@router.put("/update",response_model=UserUpdate,description="用户修改个人信息")
async def user_update(user_in:UserUpdate,
                      db:AsyncSession = Depends(get_async_db),
                      current_user:dict =Depends(get_current_user)
                      ):
    # 从current_user字典中获取用户ID
    user_id = current_user.get("user_id")
    if user_id is None:
        raise HTTPException(status_code=400, detail="Invalid user ID")

    # 调用数据库操作函数更新用户资料,要求传入用户ID和新的用户信息
    user = await update_user(db=db, user_id=user_id, user_in=user_in)
    return user

# 用户获取顾问列表接口
@router.get("/get_advisor",response_model=List[AdvisorList],description="获取顾问列表")
async def user_getadvisorlist(
    cursor_id: int = Query(None), # cursor_id参数：用作下一批数据开始点的标识
    limit: int = Query(4, ge=1,le=4), # limit参数：每次加载的顾问数量
    db: AsyncSession = Depends(get_async_db)
):
    if cursor_id is not None:
        advisors = await get_advisors_after_cursor(db=db, cursor_id=cursor_id, limit=limit)
    else:
        # 如果没有提供cursor_id，则从头开始
        advisors = await get_paged_advisors(db=db, page=1, page_size=limit)
    return [AdvisorList(id=advisor.id,name=advisor.name, bio=advisor.bio) for advisor in advisors]

# 用户查看顾问主页接口
@router.get("/advisor/{advisor_id}", response_model=AdvisorDetailed,description= "查看顾问主页")
async def advisor_detail(
    advisor_id: int = Path(..., title="The ID of the advisor to get details for"),
    db: AsyncSession = Depends(get_async_db)
):
    advisordetail = await get_advisor_detail(db=db,advisor_id=advisor_id)
    
    return advisordetail    


