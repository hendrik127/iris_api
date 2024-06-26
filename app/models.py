"""
This module defines the Iris data model for storing information about iris flowers.

The Iris model includes attributes for the sepal and petal measurements, species classification,
and outlier status. It is designed to be used with an SQL database via SQLModel.
"""
from typing import Optional
from sqlmodel import SQLModel, Field


class Iris(SQLModel, table=True):
    """
    Represents an Iris flower with attributes for sepal and petal measurements,
    species classification, and outlier status.
    """
    id: Optional[int] = Field(default=None, primary_key=True)
    sepal_length: float
    sepal_width: float
    sepal_ratio: Optional[float]
    petal_length: float
    petal_width: float
    petal_ratio: Optional[float]
    species: str
    is_outlier: Optional[bool]
