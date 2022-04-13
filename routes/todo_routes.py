from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db

from models.todo_models import TodoModel
from schema.todo_schema import TodoSchema
        
router = APIRouter(
    prefix="/todo",
    tags=["Todo"]
)

@router.get("/")
async def get_todos(db:Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

@router.get("/{id}")
async def get_todo(id:int, db:Session = Depends(get_db)):
    todo = db.query(TodoModel).get(id)

    if todo is None:
        raise HTTPException(status_code=404,detail="Todo not Found")
    return todo
    

@router.post("/")
async def add_todo(todo:TodoSchema, db:Session = Depends(get_db)):
    new_todo = TodoModel(todo=todo.todo,complete=todo.complete)
    db.add(new_todo)
    db.commit()
    return {"message": "{} is Added".format(new_todo.todo)}

@router.patch("/{id}")
async def patch_todo(id:int, db:Session = Depends(get_db)):
    todo = db.query(TodoModel).get(id)

    if todo is None:
        raise HTTPException(status_code=404,detail="Todo not Found")
        
    todo.complete = not todo.complete
    db.commit()

    return todo,status.HTTP_200_OK

@router.delete("/{id}")
async def delete_todo(id:int, db:Session = Depends(get_db)):
    todo = db.query(TodoModel).get(id)

    if todo is None:
        raise HTTPException(status_code=404,detail="Todo not Found")

    db.delete(todo)
    db.commit()

    return status.HTTP_200_OK