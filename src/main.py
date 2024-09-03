from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.controller.user_controller import user_router
from src.config.database import Database
from src.utils.init_tables import InitializeTables


@asynccontextmanager
async def lifespan() -> None:
    db = Database.initialize_database()
    tables = InitializeTables(database=db)
    tables.drop_tables()


app = FastAPI()

app.include_router(user_router)
