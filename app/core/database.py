"""
This module manages initial database operations for Iris data.

It defines functions to create database tables if they do not exist,
populate the database with fetched and transformed iris data, and
validate the data structure before committing it to the database.

"""
import os
from typing import List
from sqlmodel import SQLModel, create_engine
from sqlmodel import Session, select
from pydantic import TypeAdapter, ValidationError
from dotenv import load_dotenv
from models import Iris
from fetch_transform_data import fetch_and_transform_iris_data

load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'example.env'))


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)


def create_tables() -> None:
    """
    Create database tables if they do not exist.
    Populates database if data does not exist.
    """
    SQLModel.metadata.create_all(engine)

    with Session(engine) as session:
        irises = select(Iris)
        result = session.exec(irises).first()
        if not result:
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
        except ValidationError as e:
            print(e)
        for iris in result:
            session.add(iris)
        session.commit()
