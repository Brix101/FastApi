from datetime import date
from pydantic import BaseModel

class TodoSchema(BaseModel):
    todo : str
    complete : bool | None = False

    class Config:
        orm_mode = True