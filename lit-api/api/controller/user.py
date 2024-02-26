from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from database.database import get_session
from database.orm.user.model import UserRead
from database.orm.user.crud import (
    read_users,
)

router = APIRouter()


@router.get("", response_model=list[UserRead])
def get_users(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    return read_users(offset=offset, limit=limit, db=db)
