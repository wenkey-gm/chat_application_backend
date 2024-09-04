from contextlib import asynccontextmanager

from fastapi import FastAPI
from src.controller.user_controller import user_router
from src.config.database import Database
from src.utils.init_tables import InitializeTables
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan() -> None:
    db = Database.initialize_database()
    tables = InitializeTables(database=db)
    tables.drop_tables()


app = FastAPI()

origins = [
    "http://localhost:3000", 
    "http://127.0.0.1:3000", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,  
    allow_methods=["*"], 
    allow_headers=["*"], 
)

app.include_router(user_router)
