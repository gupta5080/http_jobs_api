import mysql.connector

def get_db_connection():
    """
    Establishes a connection to the MySQL database using the provided configuration.
    
    returns:
        mysql.connector.connection.MySQLConnection: A connection object to interact with the database.
    """
    return mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),   
        database= os.getenv('DB_NAME')
    )


