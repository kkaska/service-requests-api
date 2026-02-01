CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE service_requests (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    customer_id INTEGER NOT NULL REFERENCES customers(id)
);

INSERT INTO customers (name, email)
VALUES ('Jane Doe', 'jane.doe@example.com');

INSERT INTO service_requests (description, customer_id)
VALUES ('ATM malfunctioning', 1);