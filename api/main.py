from fastapi import FastAPI
from pydantic import TypeAdapter, ValidationError
from fetch_transform_data import fetch_and_transform_iris_data
from typing import List
from sqlmodel import Session, select
from database import Iris, engine  
from fastapi.middleware.cors import CORSMiddleware


from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def populate_database() -> None:
    """
        Fetches iris data, transforms it, and writes it to the database.
    """
    with Session(engine) as session:
        iris_data = fetch_and_transform_iris_data()
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
def on_startup() -> None:
    """
    Checks whether the database is populated.
    Populates if necessary.
    """
    with Session(engine) as session:
        irises = select(Iris)
        result = session.exec(irises).first()
        if not result:
            populate_database()


@app.get("/")
async def root() -> List[Iris]:
    """Endpoint for fetching the iris data.
       Sent to user as JSON.

    Returns:
        List[Iris]: Returns a list of the irises.
    """
    with Session(engine) as session:
        result = session.exec(select(Iris)).all()
        return result
