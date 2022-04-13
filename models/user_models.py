import jwt
from sqlalchemy.schema import Column
from sqlalchemy.types import String,Integer
from database import Base


from argon2 import PasswordHasher
ph = PasswordHasher()


class UserModel(Base):
    __tablename__ = "User"

    id =Column(Integer,primary_key=True,index=True)
    username=Column(String(250),unique=True)
    password=Column(String(250))
    
    def __init__(self, username,password):
        self.username = username
        self.password = ph.hash(password)
        
    def password_match(self,password):
        return ph.verify(self.password,password)
        
    def generate_token(self):
        return jwt.encode({"id": self.id, "username": self.username},"secret", algorithm="HS256")