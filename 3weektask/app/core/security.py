# /app/core/security.py
from typing import Optional
from datetime import datetime , timedelta
from jose import jwt
from passlib.context import CryptContext
from jose.exceptions import JWTError
from fastapi.security import OAuth2PasswordBearer
from fastapi import  Depends, HTTPException, status
# 设置用于JWT的密码学签名密钥
SECRET_KEY = "rPW56wnL3ioy5HEHuD3VR2OQGGSHEBbGpZWRJ9yFKoYF"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60*24*2)
    
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=400, detail="Invalid token payload")
        return {"user_id": user_id}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_current_advisor(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        advisor_id = payload.get("sub")
        if advisor_id is None:
            raise HTTPException(status_code=400, detail="Invalid token payload")
        return {"advisor_id": advisor_id}
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid token")



