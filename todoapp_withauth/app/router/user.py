from fastapi import APIRouter ,Depends,HTTPException
from app.models import Register_User
from typing import Annotated
from app.auth import current_user, get_user_from_db,hashed_password
from app.db import get_session
from sqlmodel import Session
from app.models import User


user_router=APIRouter(
    prefix="/user",
    tags=["user"],
    responses={404:{"description":"Not Found"}}
)

@user_router.get("/")
def read_user():
    return {"message":"Welcome to Todo app user"}

# Depends() is used for
@user_router.post("/register")
def register_user(new_user:Annotated[Register_User,Depends()],session:Annotated[Session,Depends(get_session)]):
    db_user = get_user_from_db(session,new_user.username,new_user.email)
    if db_user:
        raise HTTPException(status_code=409,detail="user with these credentials already exist")
    user = User(username=new_user.username,
                email=new_user.email,
                password = hashed_password(new_user.password))
    session.add(user)
    session.commit()
    session.refresh(user)
    return {"message":f""" User with {user.username} successfully registered """}

@user_router.get("/me")
def user_profile(current_user:Annotated[User,Depends(current_user)]):
    return current_user