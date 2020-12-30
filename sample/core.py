# -*- coding: utf-8 -*-
import helpers

def event_ticket_system():
    """
    Establish database connection, handle CSV, query database, display output
    """
    csv = "csv/third_party_sales_1.csv"

    connection = helpers.get_db_connection()
    helpers.load_third_party(connection, csv)
    records = helpers.query_popular_tickets(connection)
    helpers.display_records(records)

if __name__ == "__main__":
    event_ticket_system()