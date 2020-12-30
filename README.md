## Table of Contents
- [General Info](#general-info)
- [Technologies](#technologies)
- [Setup](#setup)

## General Info
In this mini-project, I used the MySQL ```mysql-connector-python``` database adapter with Python to create a basic data pipeline. The following steps were executed:

- Setup database connection
- Read CSV file
- Load CSV file contents into table in local MySQL database
- Query the table to retrieve the selected records
- Display the result

## Technologies
Mini-project is created with: 
* Python 3.8.3
* MySQL 8.0.22

## Setup
To run this mini-project, follow the steps below:

1. ```$ git clone https://github.com/BenGriffith/event-ticket-system.git```
2. Execute sample/sql/ticket_sales_ddl.sql in MySQL
3. Setup connection information in sample/helpers.py in ```get_db_connection()```
4. 
```
$ cd sample
$ python3 core.py