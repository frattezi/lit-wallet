import uuid
from fastapi import APIRouter, Depends, Query
from sqlmodel import Session

from database.database import get_session
from public.user.models import UserCreate, UserRead, UserUpdate
from public.user.crud import (
    create_user,
    read_users,
    read_user,
    update_user,
    delete_user,
)

router = APIRouter()


@router.post("", response_model=UserRead)
def create_user_api(user: UserCreate, db: Session = Depends(get_session)):
    return create_user(user=user, db=db)


@router.get("", response_model=list[UserRead])
def get_heroes_api(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    print("Im here!")
    return read_users(offset=offset, limit=limit, db=db)


@router.get("/{user_id}", response_model=UserRead)
def get_user_api(user_id: uuid.UUID, db: Session = Depends(get_session)):
    return read_user(user_id=user_id, db=db)


@router.patch("/{hero_id}", response_model=UserRead)
def update_user_api(
    user_id: uuid.UUID, hero: UserUpdate, db: Session = Depends(get_session)
):
    return update_user(user_id=user_id, hero=hero, db=db)


@router.delete("/{user_id}")
def delete_user_api(user_id: uuid.UUID, db: Session = Depends(get_session)):
    return delete_user(user_id=user_id, db=db)
