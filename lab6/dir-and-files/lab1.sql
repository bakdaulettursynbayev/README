CREATE DATABASE lab1;

--\c lab1;

CREATE TABLE clients (
client_id SERIAL,
first_name VARCHAR(60),
last_name VARCHAR(60),
email VARCHAR(100),
date_joined DATE,
PRIMARY KEY (client_id)
);

ALTER TABLE clients
ADD status INT DEFAULT 0;

ALTER TABLE clients
ALTER COLUMN status TYPE BOOLEAN;

ALTER TABLE clients
ALTER COLUMN status SET DEFAULT TRUE;

CREATE TABLE orders (
order_id SERIAL,
order_name VARCHAR(100),
client_id INT,
PRIMARY KEY (order_id),
FOREIGN KEY (client_id) REFERENCES clients(client_id)
);

DROP TABLE orders;

DROP DATABASE lab1;