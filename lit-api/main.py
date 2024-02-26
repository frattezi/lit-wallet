from fastapi import FastAPI
from contextlib import asynccontextmanager

from .api import api as public_api
from database.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI()
app.router.lifespan_context = lifespan

app.include_router(public_api)
