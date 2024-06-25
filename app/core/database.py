from sqlmodel import SQLModel, create_engine
from fetch_transform_data import fetch_and_transform_iris_data
from sqlmodel import Session
from models import Iris
from typing import List
from pydantic import TypeAdapter, ValidationError
from dotenv import load_dotenv
import os


load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'example.env'))


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)


def create_tables():
    SQLModel.metadata.create_all(engine)
    populate_database()


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
