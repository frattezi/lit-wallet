from requests import Session
from sqlalchemy import Engine
from sqlmodel import SQLModel, create_engine

from database.seeds import seed_database

# TODO: Use environment variables to build Database URL
database_name = "finances"
DATABASE_URL = f"postgresql://postgres:passwd@localhost/{database_name}"

engine = create_engine(DATABASE_URL)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    print("Database initialized")

    seed_database(engine)

    print("Database seeded")


def get_session():
    with Session(engine) as session:
        yield session
