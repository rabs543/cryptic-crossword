import mysql.connector
from mysql.connector import Error

# Database connection details
host = 'localhost'  # or IP address of the MySQL server
port = 3306         # Default MySQL port
user = 'root'
password = 'wnz/1fSDAVdPG3FO5+ntlZ871ld2ese8'

database_name = 'crossword'

try:
    # Establishing the connection
    connection = mysql.connector.connect(
        host=host,
        port=port,
        user=user,
        password=password
    )
    
    if connection.is_connected():
        print("Successfully connected to the database")
        
        # Create a cursor object
        cursor = connection.cursor()

        # SQL to create a database
        create_db_query = "CREATE DATABASE {}".format(database_name)
        cursor.execute(create_db_query)
        print("Database '{}' created successfully".format(database_name))

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")