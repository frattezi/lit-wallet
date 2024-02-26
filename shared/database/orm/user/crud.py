import uuid
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select

from database.database import get_session
from database.orm.user.model import User, UserCreate, UserUpdate


def create_user(user: UserCreate, db: Session = Depends(get_session)):
    parser_user = User.model_validate(user)
    db.add(parser_user)
    db.commit()
    db.refresh(parser_user)

    return parser_user


def read_users(offset: int = 0, limit: int = 20, db: Session = Depends(get_session)):
    return db.exec(select(User).offset(offset).limit(limit)).all()


def read_user(user_id: uuid.UUID, db: Session = Depends(get_session)):
    user = db.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hero not found with id: {user_id}",
        )
    return user


def update_user(
    user_id: uuid.UUID, update_data: UserUpdate, db: Session = Depends(get_session)
):
    user_to_update = db.get(User, user_id)
    if not user_to_update:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hero not found with id: {user_id}",
        )

    # Apply update_data to user_to_update
    for field, value in update_data:
        setattr(user_to_update, field, value)
    validated_user = User.model_validate(user_to_update)

    db.add(validated_user)
    db.commit()
    db.refresh(validated_user)
    return validated_user


def delete_user(user_id: int, db: Session = Depends(get_session)):
    user = db.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Hero not found with id: {user_id}",
        )

    db.delete(user)
    db.commit()

    return {"ok": True}
