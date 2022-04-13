from cmath import log
from fastapi import APIRouter,Depends,status,HTTPException
from sqlalchemy.orm import Session
from database import get_db

from models.user_models import UserModel
from schema.user_schema import UserSchema

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

@router.post("/add-user")
async def add_user(user:UserSchema, db : Session = Depends(get_db)):  
    try:
        new_user = UserModel(username=user.username,password=user.password)
        db.add(new_user)
        db.commit()
        return {"message": "{} is Added".format(new_user.username)}
    except Exception as e:
        raise HTTPException(400, detail=e.orig.msg)
    
@router.post("/login")
async def login_user(user:UserSchema,db:Session = Depends(get_db)):
    login_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if(login_user is None):
            raise HTTPException(404, detail="Username Not Found")
    
    try:          
        login_user.password_match(user.password)
        
        return "Welcome {}".format(login_user.username)
    except Exception as e:
        return str(e)
    