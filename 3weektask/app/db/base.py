#app/db/base.py
'''
SQLAlchemy
定义ORM映射类的基类

'''

from sqlalchemy.orm import declarative_base

Base = declarative_base()
