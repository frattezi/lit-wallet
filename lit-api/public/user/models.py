import enum
from typing import TYPE_CHECKING, Optional
import uuid
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from wallet.models import Wallet


class UserRoles(enum.Enum):
    USER = "USER"
    ADMIN = "ADMIN"


class UserBase(SQLModel):
    name: str = Field()
    role: UserRoles = Field()

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "id": "123e456-1234-5678-1234-567812345678",
                "name": "David Banner",
                "role": "USER",
                "wallet_id": "4acd437a-c2a7-4c2f-9ea2-e0affea0e131",
            }
        }


class User(UserBase, table=True):
    id: uuid.UUID = Field(
        default=uuid.uuid4(),
        primary_key=True,
        index=True,
        nullable=False,
    )

    wallet_id: Optional[uuid.UUID] = Field(foreign_key="wallet.id")
    wallet: Optional["Wallet"] = Relationship(back_populates="user")


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: uuid.UUID
    name: str
    role: UserRoles
    wallet_id: uuid.UUID


class UserUpdate(UserBase):
    id: uuid.UUID
    name: str
