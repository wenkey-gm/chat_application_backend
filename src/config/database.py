from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database

from src.utils.constants import DATABASE_URL


class Database:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL, echo=True)
        self._create_database_if_not_exists()
        self.session_factory = sessionmaker(bind=self.engine)
        self.session = scoped_session(self.session_factory)

    def _create_database_if_not_exists(self):
        if not database_exists(self.engine.url):
            create_database(self.engine.url)
        else:
            # Optional: Establish a connection to verify the database is accessible
            with self.engine.connect() as connection:
                pass

    def get_session(self):
        session = self.session()
        try:
            print("Connection successful!")
            yield session
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()
