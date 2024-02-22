import uuid
from typing import TYPE_CHECKING, List
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from user.models import User
    from transaction.models import Transaction


class WalletBase(SQLModel):
    total: int = Field(index=True)

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "id": "123e456-1234-5678-1234-567812345678",
                "total": "10000",
            }
        }


class Wallet(WalletBase, table=True):
    id: uuid.UUID = Field(
        default=uuid.uuid4(),
        primary_key=True,
        index=True,
        nullable=False,
    )

    user: "User" = Relationship(back_populates="wallet")
    transactions: List["Transaction"] = Relationship(back_populates="wallet")


class WalletCreate(WalletBase):
    pass


class WalletRead(WalletBase):
    id: uuid.UUID
    total: int


class WalletUpdate(WalletBase):
    id: uuid.UUID
    total: int
