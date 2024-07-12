from fastapi import FastAPI,Depends,HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session,select
from typing import Annotated
from contextlib import asynccontextmanager
from app.db import create_tables,get_session
from app.models import Edit_Todo, Todo, TodoCreate, Token, User
from app.router import user
from app.auth import authenticate_user, current_user, validate_refresh_token
from datetime import timedelta
from app.auth import EXPIRY_TIME,create_Access_token


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Creating Tables")
    create_tables()
    print("after created tables")
    yield


app:FastAPI = FastAPI(lifespan=lifespan,title="Todo-App",version="1.0.0")
app.include_router(router=user.user_router)

@app.get('/')
def root():
    return {"message":"Hello World"}

# Login
@app.post("/token",response_model=Token)
def login(form_data:Annotated[OAuth2PasswordRequestForm, Depends()],
                session:Annotated[Session, Depends(get_session)]):
          user = authenticate_user (form_data.username, form_data.password,session )
          if not user:
              raise HTTPException(status_code=401,detail="Invalid email or password")
          expiry_time = timedelta(minutes=EXPIRY_TIME)
          access_token = create_Access_token({"sub":form_data.username},expiry_time)

          refresh_expiry_time = timedelta(days=7)
          refresh_token = create_Access_token({"sub":user.email},refresh_expiry_time)

          return Token(access_token=access_token,token_type="bearer",refresh_token=refresh_token)

@app.post("/token/refresh")
def refresh_token(old_refresh_token:str,session:Annotated[Session,Depends(get_session)]):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-AUTHETICATE":"Bearer"}
        )
    user = validate_refresh_token(old_refresh_token,session)
    if not user:
        raise credential_exception
    
    expiry_time = timedelta(minutes=EXPIRY_TIME)
    access_token = create_Access_token({"sub":user.username},expiry_time)

    refresh_expiry_time = timedelta(days=7)
    refresh_token = create_Access_token({"sub":user.email},refresh_expiry_time)

    return Token(access_token=access_token,token_type="bearer",refresh_token=refresh_token)
    

@app.post("/todos",response_model = Todo)
def create_todo(current_user:Annotated[User,Depends(current_user)],todo:TodoCreate,session:Annotated[Session,Depends(get_session)]):
    new_todo = Todo(content=todo.content,user_id=current_user.id)
    session.add(new_todo)
    session.commit()
    session.refresh(new_todo)
    return new_todo
    

@app.get("/todos",response_model=list[Todo])
async def get_all(current_user:Annotated[User,Depends(current_user)],session:Annotated[Session,Depends(get_session)]):
    todos = session.exec(select(Todo).where(Todo.user_id==current_user.id)).all()
    if todos:
        return todos
    else:
        raise HTTPException(status_code = 404, details = "No task found")

@app.get("/todos/{id}",response_model=Todo)
async def get_single_todo(id:int,
                          current_user:Annotated[User,Depends(current_user)],
                          session:Annotated[Session,Depends(get_session)]):
    user_todos = session.exec(select(Todo).where(Todo.user_id==current_user.id)).all()
    todo = next((todo for todo in user_todos if todo.id==id),None)
    # next is generator function
    if todo:
        return todo
    else:
        raise HTTPException(status_code = 404, details = "No task found")


@app.put("/todos/{id}")
def edit_todo(id:int,current_user:Annotated[User,Depends(current_user)],todo:Edit_Todo,session:Annotated[Session,Depends(get_session)]):
    user_todos = session.exec(select(Todo).where(Todo.user_id==current_user.id)).all()
    existing_todo = next((todo for todo in user_todos if todo.id == id),None)
    if existing_todo:
        existing_todo.content = todo.content
        existing_todo.is_Completed =todo.is_Completed
        session.add(existing_todo)
        session.commit()
        session.refresh(existing_todo)
        return existing_todo
    else:
        raise HTTPException(status_code= 404,details="Task not found")

@app.delete('/todos/{id}')
def delete_todo(id:int,current_user:Annotated[User,Depends(current_user)],session:Annotated[Session,Depends(get_session)]):
    user_todos = session.exec(select(Todo).where(Todo.user_id==current_user.id)).all()
    todo = next((todo for todo in user_todos if todo.id == id),None)
    # todo = session.get(Todo,id) same as above
    if todo:
        session.delete(todo)
        session.commit()
        return {"message":"Task deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="No task found")