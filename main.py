from fastapi import Depends, FastAPI,status,HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine,Base


from models.todo_models import TodoModel
from schema.todo_schema import TodoSchema

Base.metadata.create_all(engine)

app = FastAPI(title="Fast Api Todo App")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def get_root():
    return {"message":"Welcome to FastApi!!!"}

@app.get("/todo")
async def get_todos(db:Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return todos

@app.get("/todo/{id}")
async def get_todo(id:int, db:Session = Depends(get_db)):
    todo = db.query(TodoModel).get(id)

    if todo is None:
        raise HTTPException(status_code=404,detail="Todo not Found")
    return todo
    

@app.post("/todo")
async def add_todo(todo:TodoSchema, db:Session = Depends(get_db)):
    new_todo = TodoModel(todo=todo.todo,complete=todo.complete)
    db.add(new_todo)
    db.commit()
    return {"message": "{} is Added".format(new_todo.todo)}

@app.patch("/todo/{id}")
async def patch_todo(id:int, db:Session = Depends(get_db)):
    todo = db.query(TodoModel).get(id)

    if todo is None:
        raise HTTPException(status_code=404,detail="Todo not Found")
        
    todo.complete = not todo.complete
    db.commit()

    return todo,status.HTTP_200_OK

@app.delete("/todo/{id}")
async def delete_todo(id:int, db:Session = Depends(get_db)):
    todo = db.query(TodoModel).get(id)

    if todo is None:
        raise HTTPException(status_code=404,detail="Todo not Found")

    db.delete(todo)
    db.commit()

    return status.HTTP_200_OK