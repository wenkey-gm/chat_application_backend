# Chat Application Backend

## Overview

This is the backend for a chat application built using Python, FastApi, Docker, and Poetry. It provides functionalities like user management, real-time chat, and message storage. The application is scalable and deployable via Docker containers.

## Features

- User authentication & registration
- Real-time chat
- Message storage (MySQL)
- Dockerized for deployment
- Unit tests included(Manual running)

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/wenkey-gm/chat_application_backend.git
   cd chat_application_backend

2. Build and run the project using Docker:
   ```bash
    docker-compose up
    ```

## Dependencies

- Python 3.x
- Docker & Docker Compose
- Poetry

## Folder Structure

- **src/**: Contains the source code of the application.
- **tests/**: Integration tests create a fake sql server to run tests(not dockerized).
- **Dockerfile**: Defines the Docker image configuration.
- **docker-compose.yml**: Multi-container setup for Docker.
- **init.sql**: SQL script to initialize the PostgreSQL database.

## Database

This application uses PostgreSQL as the database, configured via `init.sql`.

