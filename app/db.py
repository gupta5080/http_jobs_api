import mysql.connector

def get_db_connection():
    """
    Establishes a connection to the MySQL database using the provided configuration.
    
    returns:
        mysql.connector.connection.MySQLConnection: A connection object to interact with the database.
    """
    return mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        user='admin',
        password='admin',   
        database='jobs'  # Optional: specify a database to connect to
    )


