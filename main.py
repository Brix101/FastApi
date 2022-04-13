from fastapi import  FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import null
from database import engine,Base
import jwt


from routes import todo_routes,user_routes

Base.metadata.create_all(engine)

app = FastAPI(title="Fast Api Todo App")

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# import routes
app.include_router(todo_routes.router)
app.include_router(user_routes.router)

@app.middleware("http")
async def token_encoder(request: Request,call_next): 
    token = request.cookies.get("session")
    if(token is not None):
        user=jwt.decode(token, "secret", algorithms=["HS256"])
    
    response.user = user
    response = await call_next(request)
    return response


@app.get("/")
async def get_root():
    return {"message":"Welcome to FastApi!!!"}

