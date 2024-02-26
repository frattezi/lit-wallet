from sqlalchemy import Engine
from sqlmodel import Session

from database.orm.user.model import User, UserRoles

# TODO: Refactor
userData = {
    "id": "5c49ade2-e01d-4b6b-b57e-5a737d050404",
    "name": "Alex",
    "role": UserRoles.ADMIN,
}


def seed_database(engine: Engine):
    with Session(engine) as session:
        database_is_seeded = session.get(User, "5c49ade2-e01d-4b6b-b57e-5a737d050404")

        # TODO: avoid needing this, use upsert instead
        if database_is_seeded:
            print("Database already seeded")
            return

        new_user = User(**userData)
        session.add(new_user)

        session.commit()

        session.refresh(new_user)
