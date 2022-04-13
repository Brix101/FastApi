from lib2to3.pytree import Base
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# username:password@localhost:port/database
DATABASE_URL = "mysql+mysqlconnector://root:root@127.0.0.2:3306/fastapi-todo-app"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base = declarative_base()