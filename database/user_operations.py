from database.db_connection import get_db_connection


def check_duplicate(email, phone):

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
    SELECT COUNT(*)
    FROM users
    WHERE email = %s
       OR phone = %s
    """

    cursor.execute(query, (email, phone))

    count = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return count > 0