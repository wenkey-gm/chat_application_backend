from src.config.database import Database
from src.models.user import User
from src.models.message import Message


class InitializeTables:
    def __init__(self, database: Database):
        self.database = database

    def create_tables(self):
        User.metadata.create_all(bind=self.database.engine)
        Message.metadata.create_all(bind=self.database.engine)

    def drop_tables(self):
        User.metadata.drop_all(bind=self.database.engine)
        Message.metadata.drop_all(bind=self.database.engine)

