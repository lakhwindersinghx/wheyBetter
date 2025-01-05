import mysql.connector
from mysql.connector import Error

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="1721",
            database="whey_protein"
        )

        if connection.is_connected():
            print("Successfully connected to MySQL!")
            db_info = connection.get_server_info()
            print("Server version:", db_info)
            connection.close()  # Close the connection to avoid resource issues

    except Error as e:
        print("Error while connecting to MySQL:", e)

connect_to_mysql()
