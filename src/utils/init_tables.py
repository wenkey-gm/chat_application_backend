from src.models.message import Message
from src.models.user import User
from src.config.database import Database


def create_tables():
    User.metadata.create_all(bind=Database.engine)
    Message.metadata.create_all(bind=Database.engine)


def drop_tables():
    User.metadata.drop_all(bind=Database.engine)
    Message.metadata.drop_all(bind=Database.engine)
