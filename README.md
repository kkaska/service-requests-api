# Service Request API
This project implements a simple, containerised backend system consisting of:
- A PostgreSQL database storing service requests and customer details
- A Python-based API providing read-only access to those service requests

---

## Brief:
Deploy an SQL database that stores service requests. The service requests must contain a description of work to be done and customer details (the values used in fields are not important).
Create a containerized API that returns specific service requests from the database.

---

## Architecture Summary

- **Database**: PostgreSQL, deployed locally via Docker Compose.
Widely used database that was suitable for this exercise as it required a relational schema.
- **API**: Python FastAPI application, containerised with Docker.
FastAPI is very lightweight and has explicit request handling and automatic request validation.   
- **Orchestration**: Docker Compose.


The database and API run as separate containers on a shared Docker network.

---

## Assumptions / Design Decisions
Application configuration is provided via environment variables.
The .env file is purposely committed to the repository for the exercise. In production these values would be managed via secrets.

Service request status values are not enforced for simplicity. In a production system there would be restricted to certain values (e.g. OPEN, IN_PROGRESS, CLOSED).

The list endpoint returns summary data only, not the full customer details.

Database setup is managed independently from the API to reflect common production scenarios.

---
## Database

### Schema

The database uses a simple relational schema:
- `customers` – stores basic customer contact details
- `service_requests` – stores service request information and references a customer

Each service request includes:
- Description of work to be done
- Status (e.g. `OPEN`, `IN_PROGRESS`)
- Creation timestamp
- Associated customer id

The schema is initialised and seeded automatically at container startup.


### Running and Inspecting the Database

Start the database:
`docker compose up -d`

Connect to PostgreSQL:
`docker exec -it service_requests_db psql -U app_user -d service_requests`

Example Queries:
`SELECT * FROM customers;`
`SELECT * FROM service_requests;`

Exit PostgreSQL:
`\q`

---

## API

### Endpoints

- GET /health
Returns a single health check response.

- GET /service-requests
Returns a summary list of all service requests

- GET /service-requests/{id}
Returns full details for a single service request, including customer details

### Running the API
Locally:
`uvicorn app.main:app --reload`
Containerised Application:
`docker compose up --build`
Test Endpoints:
`curl http://localhost:8000/health`
`curl http://localhost:8000/service-requests`
`curl http://localhost:8000/service-requests/1`

### Shutdown containers
`docker compose down -v`