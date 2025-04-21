import mysql.connector
import os

def get_db_connection():
    """
    Establishes a connection to the MySQL database using the provided configuration.
    
    returns:
        mysql.connector.connection.MySQLConnection: A connection object to interact with the database.
    """
    print("INFO: Connecting to the database...")
    print("INFO: DB_HOST:", os.getenv('DB_HOST'))
    print("INFO: DB_PORT:", os.getenv('DB_PORT'))
    print("INFO: DB_USER:", os.getenv('DB_USER'))
    print("INFO: DB_PASSWORD:", os.getenv('DB_PASSWORD'))
    print("INFO: DB_NAME:", os.getenv('DB_NAME'))
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),   
        database= os.getenv('DB_NAME')
    )


