import enum
from typing import TYPE_CHECKING
import uuid
from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from api.public.wallet.models import Wallet


class TransactionType(enum.Enum):
    INCOME = "INCOME"
    OUTCOME = "OUTCOME"


class TransactionBase(SQLModel):
    amount: int = Field(index=True)
    type: TransactionType = Field()

    class Config:
        arbitrary_types_allowed = True
        json_schema_extra = {
            "example": {
                "id": "123e456-1234-5678-1234-567812345678",
                "amount": 100,
                "type": "OUTCOME",
            }
        }


class Transaction(TransactionBase, table=True):
    id: uuid.UUID = Field(
        default=uuid.uuid4(),
        primary_key=True,
        index=True,
        nullable=False,
    )

    wallet_id: uuid.UUID = Field(foreign_key="wallet.id")
    wallet: "Wallet" = Relationship(back_populates="transactions")


class TransactionCreate(TransactionBase):
    pass


class TransactionRead(TransactionBase):
    id: uuid.UUID
    amount: int
    type: TransactionType
    wallet_id: uuid.UUID


class TransactionUpdate(TransactionBase):
    id: uuid.UUID
    amount: int
    type: TransactionType
