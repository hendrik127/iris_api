"""
Database Dependency and Session Management

This module provides utilities for managing database sessions and dependencies
within a FastAPI application. It defines a database session generator function
and an annotated type alias for dependency injection.
"""
from typing import Annotated
from collections.abc import Generator
from sqlmodel import Session
from fastapi import Depends
from core.database import engine


def get_db() -> Generator[Session, None, None]:
    """
    Generator function yielding a database session.

    This function manages the lifecycle of a SQLModel Session using 
    the database engine imported from core.database.
    It creates a session, yields it for use in the dependent function,
    and ensures the session is properly closed when the generator is exited.

    Yields:
        Session: A database session object.
    """

    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
