from sqlalchemy.schema import Column
from sqlalchemy.types import String,Integer
from database import Base

class UserModel(Base):
    __tablename__ = "User"

    id =Column(Integer,primary_key=True,index=True)
    username=Column(String(250),unique=True)
    password=Column(String(250))
    
    