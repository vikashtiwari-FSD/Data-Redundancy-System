import mysql.connector
from config import DB_CONFIG


def get_db_connection():
    """
    Creates and returns a connection to the MySQL database.
    """

    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )

        if connection.is_connected():
            print("✅ Database connected successfully!")

        return connection

    except mysql.connector.Error as err:
        print(f"❌ Database Connection Error: {err}")
        return None