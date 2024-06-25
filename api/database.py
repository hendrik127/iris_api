from sqlmodel import SQLModel, create_engine, Field
from typing import Optional
from dotenv import load_dotenv
import os


load_dotenv(os.path.join(os.path.dirname(__file__), '..', 'example.env'))


DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)


class Iris(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    sepal_length: float
    sepal_width: float
    sepal_ratio: Optional[float]
    petal_length: float
    petal_width: float
    petal_ratio: Optional[float]
    species: str
    is_outlier: Optional[bool]


def create_tables():
    SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    create_tables()
