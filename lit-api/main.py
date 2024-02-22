from fastapi import Depends, FastAPI, Query
from contextlib import asynccontextmanager

from requests import Session

from database.database import create_db_and_tables, get_session


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    yield


app = FastAPI()
app.router.lifespan_context = lifespan


@app.get("/users")
async def read_users(
    offset: int = 0,
    limit: int = Query(default=100, lte=100),
    db: Session = Depends(get_session),
):
    print("Im here!")
    return read_users(offset=offset, limit=limit, db=db)
