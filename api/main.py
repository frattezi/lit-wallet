from fastapi import FastAPI
from contextlib import asynccontextmanager

from api.database.database import create_db_and_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI()
app.router.lifespan_context = lifespan


@app.get("/users/")
async def read_users():
    pass


@app.post("/users/")
async def create_users():
    pass
