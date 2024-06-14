# Book Management FastAPI

## Prerequisites
Before proceeding, ensure you have Docker and Docker Compose installed on your machine.

- Docker
- Docker Compose

## Installation

- Clone the repository

## Running the Application
To start the application along with any necessary services (like databases), simply run:
```
docker-compose up --build
```

- This command builds (if necessary) and starts all services and tests defined in docker-compose.yml file.
- By default, the FastAPI application will be accessible at  [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## API docs
You can access to automatically generated API documentation at
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) provided by Swagger
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) provided by ReDoc
