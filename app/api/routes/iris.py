"""
This module defines the API endpoints for interacting with the Iris dataset.

Endpoints:
- /outliers: Retrieves a list of Iris records that are marked as outliers.
- /cleaned: Retrieves a list of Iris records that are not marked as outliers.
- /{species}: Retrieves a list of Iris records of a specified species or all.

Each endpoint returns the data as JSON to the user.

"""
from typing import List
from fastapi import APIRouter, HTTPException
from sqlmodel import select
from models import Iris
from api.dependencies import SessionDep

router = APIRouter()


@router.get("/outliers")
async def get_outlier_irises(session: SessionDep) -> List[Iris]:
    """Endpoint for outliers.
       Sent to user as JSON.

    Returns:
        List[Iris]: Returns a list of irises that are outliers.
    """
    result = session.exec(select(Iris).where(Iris.is_outlier)).all()
    return result


@router.get("/cleaned")
async def get_cleaned_irises(session: SessionDep) -> List[Iris]:
    """Endpoint for outliers removed.
       Sent to user as JSON.

    Returns:
        List[Iris]: Returns a list of irises that are outliers.
    """
    result = session.exec(select(Iris).where(
        Iris.is_outlier == False)).all()  # pylint: disable=C0121
    return result


@router.get("/{species}")
async def get_irises(session: SessionDep, species: str) -> List[Iris]:
    """Endpoint for fetching the iris data.
       Sent to user as JSON.

    Returns:
        List[Iris]: Returns a list of irises of a certain species or all.
    """
    if species != 'all':
        result = session.exec(select(Iris).where(
            Iris.species == species)).all()
    else:
        result = session.exec(select(Iris)).all()
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Species {species} not found")
    return result
