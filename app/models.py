from typing import Optional
from sqlmodel import SQLModel, Field


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
