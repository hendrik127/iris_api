from fastapi import APIRouter, HTTPException
from typing import List
from models import Iris
from api.dependencies import SessionDep
from sqlmodel import select

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
    result = session.exec(select(Iris).where(Iris.is_outlier != True)).all()
    return result


@router.get("/{species}")
async def get_irises(session: SessionDep, species: str) -> List[Iris]:
    """Endpoint for fetching the iris data.
       Sent to user as JSON.

    Returns:
        List[Iris]: Returns a list of irises of a certain species or all.
    """
    if species != 'all':
        result = session.exec(select(Iris).where(Iris.species == species)).all()
    else:
        result = session.exec(select(Iris)).all()
    
    if not result:
        raise HTTPException(status_code=404, detail=f"Species {species} not found")
    return result


# @router.get("{top_bottom}/{n}/{feature}", response_model=List[Iris])
# def fetch_top_five_longest_irises(session: SessionDep) -> List[Iris]:
#     result = session.exec(
#             select(Iris).order_by(Iris.sepal_length.desc()).limit(5)
#         ).all()
#     return result