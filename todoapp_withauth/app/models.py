from sqlmodel import SQLModel,Field
from fastapi import Form
from typing import Annotated
from pydantic import BaseModel

class Todo(SQLModel,table=True):
    id:int | None = Field(default=None,primary_key=True)
    content:str = Field(index=True,min_length = 5,max_length = 54)
    is_Completed:bool = Field(default=False)
    user_id:int = Field(foreign_key="user.id")

class User(SQLModel,table=True):
     id:int | None = Field(default=None,primary_key=True)
     username:str
     email:str
     password:str

class Register_User(BaseModel):
     username: Annotated[
            str,
            Form(),
     ]
     email: Annotated[
            str,
            Form(),
     ]
     password: Annotated[
            str,
            Form(),
     ]

class Token(BaseModel):
     access_token:str
     token_type:str
     refresh_token:str 

class TokenData(BaseModel):
     username:str
     
class Refresh_TokenData(BaseModel):
     email:str

class TodoCreate(BaseModel):
    content:str = Field(index=True,min_length = 5,max_length = 54)

class Edit_Todo(BaseModel):
     content:str
     is_completed:bool
