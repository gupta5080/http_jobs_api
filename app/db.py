import mysql.connector
import os
import logging

def get_db_connection():
    """
    Establishes a connection to the MySQL database using the provided configuration.
    
    returns:
        mysql.connector.connection.MySQLConnection: A connection object to interact with the database.
    """
    logger = logging.getLogger(__name__)
    try:
        logger.info("Connecting to the database...")
        logger.info("DB_HOST: %s", os.getenv('DB_HOST'))
        logger.info("DB_PORT: %s", os.getenv('DB_PORT'))
        logger.info("DB_USER: %s", os.getenv('DB_USER'))
        connection = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            database=os.getenv('DB_NAME')
        )
        logger.info("Database connection established successfully.")
        return connection
    except mysql.connector.Error as err:
        logger.error("Error connecting to the database: %s", err)
        raise


