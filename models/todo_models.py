from sqlalchemy.schema import Column
from sqlalchemy.types import String,Integer,Text,Boolean
from database import Base,engine


class TodoModel(Base):
    __tablename__ = "Todo"

    id =Column(Integer,primary_key=True,index=True)
    todo=Column(String(250))
    complete=Column(Boolean,default=False)
    
    