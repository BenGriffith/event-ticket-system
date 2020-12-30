import mysql.connector

def get_db_connection():
    """
    Establish database connection
    """
    connection = None

    config = {
        "user": "",
        "password": "",
        "host": "",
        "port": "3306",
        "database": "ticket"
    }

    try:
        connection = mysql.connector.connect(**config)
    except Exception as error:
        print("Error while connecting to database for job tracker", error)
    
    return connection

def load_third_party(connection, file_path_csv):
    """
    Read CSV file and insert into ticket_sales table
    """
    
    cursor = connection.cursor()

    with open(file_path_csv, "r") as csv:

        for line in csv:

            # Convert CSV record into a list
            ticket = line.strip().split(",")

            # Insert statement for ticket_sales
            add_ticket = ("INSERT INTO ticket_sales "
            "(ticket_id, trans_date, event_id, event_name, event_date, event_type, event_city, customer_id, price, num_tickets) "
            "VALUES (%(ticket_id)s, %(trans_date)s, %(event_id)s, %(event_name)s, %(event_date)s, %(event_type)s, %(event_city)s, %(customer_id)s, %(price)s, %(num_tickets)s)")

            # Ticket sale data to insert using add_ticket
            ticket_dict = {
                "ticket_id": ticket[0],
                "trans_date": ticket[1],
                "event_id": ticket[2],
                "event_name": ticket[3],
                "event_date": ticket[4],
                "event_type": ticket[5],
                "event_city": ticket[6],
                "customer_id": ticket[7],
                "price": ticket[8],
                "num_tickets": ticket[9]
            }

            # Insert ticket_dict into add_ticket
            cursor.execute(add_ticket, ticket_dict)

    connection.commit()
    cursor.close()
    return

def query_popular_tickets(connection):
    """
    Establish database connection, execute query and return result set
    """

    sql_statement = "SELECT event_name FROM ticket_sales"
    cursor = connection.cursor()
    cursor.execute(sql_statement)
    records = cursor.fetchall()
    cursor.close()
    return records

def display_records(records):
    """
    Display records returned from database query
    """

    print("Here are the events that occurred in the last 3 months:")

    for record in records:
        print("- {}".format(record[0]))