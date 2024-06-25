from fastapi import APIRouter
from typing import List
from models import Iris
from api.dependencies import SessionDep
from sqlmodel import select

router = APIRouter()

@router.get("/")
async def get_irises(session: SessionDep) -> List[Iris]:
    """Endpoint for fetching the iris data.
       Sent to user as JSON.

    Returns:
        List[Iris]: Returns a list of the irises.
    """
    result = session.exec(select(Iris)).all()
    return result
