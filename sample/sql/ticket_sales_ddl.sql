CREATE DATABASE ticket;

CREATE TABLE ticket.ticket_sales
(
	ticket_id INT PRIMARY KEY,
    trans_date DATE,
    event_id INT,
    event_name CHAR(50),
    event_date DATE,
    event_type CHAR(10),
    event_city CHAR(20),
    customer_id INT,
    price DECIMAL,
    num_tickets INT
);