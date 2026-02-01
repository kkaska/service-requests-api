CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT,
    address TEXT
);

CREATE TABLE service_requests (
    id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    status TEXT NOT NULL DEFAULT 'OPEN',
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    customer_id INTEGER NOT NULL REFERENCES customers(id)
);

-- Seed customers
INSERT INTO customers (first_name, last_name, email, phone, address)
VALUES
    (
        'Jane',
        'Doe',
        'jane.doe@example.com',
        '+44 1234 567890',
        '123 High Street, Dundee'
    ),
    (
        'John',
        'Smith',
        'john.smith@example.com',
        '+44 1234 567891',
        '123 Princes Street, Edinburgh'
    );

-- Seed service requests
INSERT INTO service_requests (description, status, customer_id)
VALUES
    (
        'ATM screen not responding',
        'OPEN',
        1
    ),
    (
        'Credit card reader showing error message',
        'IN_PROGRESS',
        2
    );