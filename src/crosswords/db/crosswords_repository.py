import mysql.connector
from mysql.connector import Error

# Database connection details
host = 'localhost'  # or IP address of the MySQL server
port = 3306         # Default MySQL port
database = 'your_database_name'
user = 'mysql'
password = 'wnz/1fSDAVdPG3FO5+ntlZ871ld2ese8'

try:
    # Establishing the connection
    connection = mysql.connector.connect(
        host=host,
        port=port,
        database=database,
        user=user,
        password=password
    )
    
    if connection.is_connected():
        print("Successfully connected to the database")
        
        # Get database info
        db_info = connection.get_server_info()
        print("MySQL Server version:", db_info)

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")