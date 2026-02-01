# Service Request API

## Brief:
Deploy an SQL database that stores service requests. The service requests must contain a description of work to be done and customer details (the values used in fields are not important).
Create a containerized API that returns specific service requests from the database.

## Containerised postgreSQL databaase with minimal relational tables
PostgreSQL database deployed via Docker Compose with basic relational schema and seed data implemented on runtime.
Relies on environment secrets for modularity & security. (.env kept public for exercise)
### Testing
`docker compose up -d`
`docker ps`
enter psql: 
`docker exec -it service_requests_db psql -U app_user -d service_requests`
interact with DB (e.g. `SELECT * FROM customers;`, `SELECT * FROM service_requests;`)
exit psql: 
`\q`

## Containserised service request API
Supports `/health` & `/service-requests/{request_id}` endpoints.

### Testing
run api locally: 
`uvicorn app.main:app --reload`
Run the containerised application: 
`docker compose up --build`
Call endpoints:
`curl http://localhost:8000/health` 
`curl http://localhost:8000/service-requests/1`