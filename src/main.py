from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.controller.message_controller import message_router
from src.controller.user_controller import user_router
from src.config.database import Database
from src.utils.init_tables import create_tables, drop_tables
from fastapi.middleware.cors import CORSMiddleware


@asynccontextmanager
async def lifespan(app: FastAPI):
    Database.initialize_database()
    # create_tables()
    # drop_tables()
    yield
    Database.session.close()


app = FastAPI(lifespan=lifespan)


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

app.include_router(user_router, prefix="/api")
app.include_router(message_router, prefix="/api")
