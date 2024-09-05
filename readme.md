# Chat Application Backend

## Overview

This is the backend for a chat application built using Python, FastApi, Docker, and Poetry. It provides functionalities like user management, real-time chat, and message storage. The application is scalable and deployable via Docker containers.

## Features

- User authentication & registration
- Real-time chat
- Message storage (MySQL)
- Dockerized for deployment
- Unit tests included(Not Dockerized)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/wenkey-gm/chat_application_backend.git
   cd chat_application_backend
   ```

2. Build and run the project using Docker:
   ```bash
    docker-compose up --build
    ```

## Local Machine Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/wenkey-gm/chat_application_backend.git
   cd chat_application_backend
   ```
   
2. Install dependencies:
   ```bash
   poetry install
   ```
3. Create .env file and paste the following:
   ```
   DB_USER="root"
   DB_PASSWORD="secret"
   DB_NAME="chat_application"
   DB_HOST=db
   DB_PORT="3306"
   TEST_DB_NAME="chat_application_test"
   ```
4. Run the application: 
   ```bash
   poetry run uvicorn src.main:app --reload
   ```
4. Access the application docs:
   ```
   http://127.0.0.1:8000/docs
   ```
## To run testcases

1. Create a database called `chat_application_test`.
2. Create `users` and `messages` tables
3. Insert data into tables:
   ```
   Insert into users(email, password) values ("one@gmail.com", "12345678");
   Insert into messages(content,is_received,user_id) values ("Hello test", True, 1);
   ```
4. To Run Test cases:
   ```bash
   poetry run pytest
   ```

## Dependencies

- Python 3.x
- Docker
- Poetry
- black

## Folder Structure

- **src/**: Contains the source code of the application.
- **tests/**: Integration tests create a fake sql server to run tests(not dockerized).
- **Dockerfile**: Defines the Docker image configuration.
- **docker-compose.yml**: Multi-container setup for Docker.
- **init.sql**: SQL script to initialize the MySql database.

## Database

This application uses MySql as the database, configured via `init.sql`.

