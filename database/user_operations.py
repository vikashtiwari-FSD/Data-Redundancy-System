from database.db_connection import get_db_connection


def check_duplicate(email, phone):

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
    SELECT *
    FROM users
    WHERE email = %s
    OR phone = %s
    """

    cursor.execute(query, (email, phone))

    existing_user = cursor.fetchone()

    cursor.close()
    connection.close()

    return existing_user