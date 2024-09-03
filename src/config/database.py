from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy_utils import database_exists, create_database

from src.utils.constants import DATABASE_URL


class Database:
    engine = create_engine(DATABASE_URL, echo=True)
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)

    @classmethod
    def initialize_database(cls):
        if not database_exists(cls.engine.url):
            create_database(cls.engine.url)
        else:
            # Optional: Establish a connection to verify the database is accessible
            with cls.engine.connect() as connection:
                pass

    @classmethod
    def get_session(cls):
        session = cls.session()
        try:
            print("Connection successful!")
            yield session
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()
        finally:
            session.close()
