import mysql.connector
from config import Config

def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host=Config.MYSQL_HOST,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DB
        )
        print("Database connection successful!")
        return conn
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

if __name__ == "__main__":
    connect_to_database()
