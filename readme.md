# Chat Application Backend

## Overview

This is the backend for a chat application built using Python, FastApi, Docker, and Poetry. It provides functionalities like user management, real-time chat, and message storage. The application is scalable and deployable via Docker containers.

## Features

- User authentication & registration
- Real-time chat
- Message storage (MySQL)
- Dockerized for deployment
- Unit tests included(Not Dockerized)

## Prerequisites

Before you start, ensure you have the following installed on your local machine:

- **Python 3.x**: Ensure you have Python installed. [Download Python](https://www.python.org/downloads/)
- **Docker**: For containerization. [Download Docker](https://www.docker.com/products/docker-desktop)
- **Poetry**: Dependency manager for Python projects. [Install Poetry](https://python-poetry.org/docs/#installation)

## Run Application(Docker)

1. Clone the repository:
   ```bash
   git clone https://github.com/wenkey-gm/chat_application_backend.git
   cd chat_application_backend
   ```

2. Build and run the project using Docker:
   ```bash
    docker-compose up --build
    ```
3. Access the application:

   Once the containers are up, the backend will be accessible at `http://localhost:8000`.

4. Access API Documentation:

   The FastAPI automatically generates interactive API documentation. You can access it via:
   ```
   http://localhost:8000/docs
   ```

## Run Application(Local Machine Setup)

1. Clone the repository:
   ```bash
   git clone https://github.com/wenkey-gm/chat_application_backend.git
   cd chat_application_backend
   ```
   
2. Install dependencies:
   ```bash
   poetry install
   ```
   
3. Run the application: 
   ```bash
   poetry run uvicorn src.main:app --reload
   ```
   
4. Access the application docs:
   ```
   http://127.0.0.1:8000/docs
   ```
## Environment Variables
   The backend requires certain environment variables for proper functioning. These should be set in a .env file.
   ```
   DB_USER="root"
   DB_PASSWORD="secret"
   DB_NAME="chat_application"
   DB_HOST="localhost"   # Use 'db' for Docker setup
   DB_PORT="3306"
   TEST_DB_NAME="chat_application_test"
   ```
   These variables are used for:

   - DB_USER: MySQL username
   - DB_PASSWORD: MySQL password
   - DB_NAME: The main database name
   - DB_HOST: Database host (db for Docker, localhost for local setup)
   - DB_PORT: MySQL port (default is 3306)
   - TEST_DB_NAME: Test database name for running test cases

## Running test cases

To ensure the correctness of the code, you can run unit tests. Note that the test setup requires a test database.
1. Set up the test database:
   Create a database called `chat_application_test` and create the necessary `users` and `messages` tables.
   ```
   CREATE DATABASE chat_application_test;
   USE chat_application_test;

   CREATE TABLE users (
     id INT AUTO_INCREMENT PRIMARY KEY,
     email VARCHAR(255) NOT NULL,
     password VARCHAR(255) NOT NULL
   );
   
   CREATE TABLE messages (
     id INT AUTO_INCREMENT PRIMARY KEY,
     content TEXT NOT NULL,
     is_received BOOLEAN NOT NULL,
     user_id INT,
     FOREIGN KEY (user_id) REFERENCES users(id)
   );
   
   INSERT INTO users(email, password) VALUES ("one@gmail.com", "12345678");
   INSERT INTO messages(content, is_received, user_id) VALUES ("Hello test", TRUE, 1);
   ```
   
2. To Run Test cases:
   ```bash
   poetry run pytest
   ```

## Folder Structure

- **src/**: Contains the source code of the application.
- **tests/**: Integration tests create a fake sql server to run tests(not dockerized).
- **Dockerfile**: Defines the Docker image configuration.
- **docker-compose.yml**: Multi-container setup for Docker.
- **init.sql**: SQL script to initialize the MySql database.

## Database

This application uses MySql as the database, configured via `init.sql`.

