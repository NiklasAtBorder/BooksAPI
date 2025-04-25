from contextlib import asynccontextmanager
from fastapi import FastAPI
from .routers import books
from .db.database import create_db


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Startataan")
    #luo tíetokanta
    create_db()
    yield
    print("Lopetellaan")


app = FastAPI(lifespan=lifespan)

app.include_router(books.router)

    



