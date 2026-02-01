# Brief:

We are looking forward to our scheduled interview. In preparation for this, please complete the following exercise. During the interview you will be asked to share your work, and follow-up questions will be asked. The below tasks must be completed to a level of quality that demonstrates your skills:
Deploy an SQL database that stores service requests. The service requests must contain a description of work to be done and customer details (the values used in fields are not important).
Create a containerized API that returns specific service requests from the database.



## Q's:
1. Do you have a preferred SQL database that should be used?
2. When you say to deploy the SQL database, is it ok to have the database setup locally or do you expect the database to be hosted somewhere?
3. For the API, is the expectation to have a minimal read-only endpoint (e.g. GET {/request/{id}) or should it support multiple endpoints?

No specific SQL engine is expected, however please base your decision on what data you are planning to store in the database, and be prepared to explain why you made that decision.
Locally configured database is sufficient, we are not expecting you to deploy anything in the cloud.
Minimal read-only is sufficient, but please feel free to expand the capability.



# Task 1: containerised postgreSQL db with minimal relational tables.
PostgreSQL database deployed locally via Docker Compose with basic relational schema and seed data impelemented on runtime.
Note - maybe add environment secrets, currently just usind default username and password for testing.
## DB Setup:
1. run docker compose script: `docker compose up -d`
2. confirm running: `docker ps`
3. enter psql: `docker exec -it service_requests_db psql -U app_user -d service_requests`
4. interact with DB (e.g. `SELECT * FROM customers;`, `SELECT * FROM service_requests;`)
5. exit: `\q`