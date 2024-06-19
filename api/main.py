from fastapi import FastAPI
from pydantic import TypeAdapter, ValidationError
from fetch_data import fetch_iris_data
from typing import List
from sqlmodel import Session, select
from database import Iris, engine  
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def populate() -> None:
    with Session(engine) as session:
        iris_data = fetch_iris_data()
        iris_list_adapter = TypeAdapter(List[Iris])
        try:
            result = iris_list_adapter.validate_json(iris_data)
            print(result)
        except ValidationError as e:
            print(e)
        for iris in result:
            session.add(iris)
        session.commit()


@app.on_event("startup")
def on_startup():
    with Session(engine) as session:
        irises = select(Iris)
        result = session.exec(irises).first()
        if not result:
            populate()


@app.get("/")
async def root() -> List[Iris]:
    with Session(engine) as session:
        result = session.exec(select(Iris)).all()
        return result
