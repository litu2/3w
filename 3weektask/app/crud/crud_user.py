#app/crud/crud_user.py
'''
对用户进行的crud操作
'''
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate,UserUpdate
from app.core.security import get_password_hash
from sqlalchemy.future import select


# 根据手机号查询用户
async def get_user_by_mobile(db: AsyncSession, mobile: str):
    # 准备异步查询
    stmt = select(User).filter(User.mobile == mobile)
    # 执行异步查询
    result = await db.execute(stmt)
    # 通过调用 .scalars().first() 来获得第一个结果
    user =  result.first()
    # 返回用户对象或: None（如果没有找到任何用户）
    return user


#  在数据库中插入一点用户数据实现注册功能
async def create_user(db: AsyncSession, user: UserCreate):
    # 密码哈希处理
    hashed_password = get_password_hash(user.password)  
    # 创建User模型对象 
    db_user = User(mobile=user.mobile,hashed_password=hashed_password)  
    db.add(db_user)  # 将用户对象添加到数据库会话中
    await db.commit()  # 提交事务
    await db.refresh(db_user)  # 刷新对象状态
    return {"msg":"create successful"}  # 返回已创建的用户对象



async def update_user(db: AsyncSession, user_id: int, user_in: UserUpdate):
    # 首先尝试找到用户
    result = await db.execute(select(User).filter(User.id == user_id))
    user = result.scalar_one_or_none()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )

    # 取用户提交的数据更新用户对象
    user_data = user_in.dict(exclude_unset=True)
    for field, value in user_data.items():
        setattr(user, field, value)

    db.add(user)  # 添加到session 中准备对数据库进行操作
    await db.commit()  # 提交数据库会话中的所有事务
    await db.refresh(user)  # 刷新user对象以反映数据库更新
    return UserUpdate(**user_data)
