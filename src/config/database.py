from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

from src.utils.constants import DATABASE_URL


class Database:

    def __init__(self):
        engine = create_engine(DATABASE_URL, echo=True)

        if not database_exists(engine.url):
            create_database(engine.url)
        else:
            engine.connect()

        session_factory = sessionmaker(bind=engine)
        session = session_factory()

        try:
            print("Connection successful!")
            yield session
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            session.close()
