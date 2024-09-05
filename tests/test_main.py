import unittest

from fastapi.testclient import TestClient
from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker

from src.config.database import Database
from src.main import app
from src.models.message import Message
from src.models.user import User
from src.utils.constants import TEST_DATABASE_URL

SQLALCHEMY_DATABASE_URL = TEST_DATABASE_URL

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

User.metadata.create_all(bind=engine)
Message.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[Database.get_session] = override_get_db

client = TestClient(app)


class TestUserLogin(unittest.TestCase):

    def test_login(self):
        login_data = {
            "email": "one@gmail.com",
            "password": "12345678"
        }
        response = client.post(
            "/api/login/",
            json=login_data,
        )
        assert response.status_code == 200
        assert response.json() == {'id': 1, 'email': 'one@gmail.com', 'is_success': True}

    def test_get_user_messages(self):
        response = client.get(
            "/api/one@gmail.com/messages",
        )
        assert response.status_code == 200
        assert response.json() is not None

    def test_create_message(self):
        message_data = {
            "content": "Hello Test",
            "is_received": True,
            "user_id": 1,
        }
        response = client.post(
            "/api/message/",
            json=message_data,
        )
        assert response.status_code == 201
        assert response.json() is not None


if __name__ == "__main__":
    unittest.main()
