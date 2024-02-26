import enum
import uuid
from sqlmodel import Field, SQLModel


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
            }
        }


class User(UserBase, table=True):
    id: uuid.UUID = Field(
        default=uuid.uuid4(),
        primary_key=True,
        index=True,
        nullable=False,
    )


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    id: uuid.UUID
    name: str
    role: UserRoles


class UserUpdate(UserBase):
    id: uuid.UUID
    name: str
