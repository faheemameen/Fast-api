from fastapi import FastAPI,Depends
from app import settings
from typing import Annotated
from sqlmodel import SQLModel,Field,create_engine,Session,select
from contextlib import asynccontextmanager

# Annotated used for custom typing
# Depends used for dependency injection

# Database table schema
class Todo(SQLModel,table=True):
    id:int | None = Field(default=None, primary_key=True)
    title:str

# Connection with database
# psycopg is a driver making a connection with database
# 1st we convert the database_url into str then we use anywhere b/c we cast secret 
connection_string:str = str(settings.DATABASE_URL).replace("postgresql","postgresql+psycopg")

engine = create_engine(connection_string)

def create_db_table():
    print("creating tables")
    SQLModel.metadata.create_all(engine)

# first run this function and call create_db_table and then after yield server will start
@asynccontextmanager
async def lifespan(app:FastAPI):
    print("server startup")
    create_db_table()
    print("after yield")
    yield

app:FastAPI = FastAPI(lifespan=lifespan)

# making separate function fo session b/c of frquently used
def get_session():
     with Session(engine) as session:
          yield session
          


@app.get("/")
def get():
    create_db_table()
    return {"msg":"Hello World"}

@app.get("/db")
def db_var():
    return {"DB":settings.DATABASE_URL,"Connection":connection_string}

@app.post("/todo")
def create_data(todo_data:Todo,session:Annotated[Session,Depends(get_session)]):
    # with Session(engine) as session:
        session = Session(engine)
        session.add(todo_data)
        session.commit()
        session.refresh(todo_data)
        session.close()
        return todo_data

# Get All Todos
@app.get("/todo")
def get_Data():
# with use of this you don't need to close manually b/c use of with block it close itself 
# when with block execute completely and
     with Session(engine) as session:
          query = select(Todo)
          all_todos = session.exec(query).all()
          return all_todos

#  if you use this way you need to close manually connection(means session.close)
     session = Session(engine)
     query = select(Todo)
     all_todos = session.exec(query).all()
     session.close()
     return all_todos
     
     

