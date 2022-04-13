from fastapi import Depends, FastAPI,status,HTTPException
from sqlalchemy.orm import Session
from database import engine,Base

from routes import todo_routes,user_routes

Base.metadata.create_all(engine)

app = FastAPI(title="Fast Api Todo App")

# import routes
app.include_router(todo_routes.router)
app.include_router(user_routes.router)


@app.get("/")
async def get_root():
    return {"message":"Welcome to FastApi!!!"}

