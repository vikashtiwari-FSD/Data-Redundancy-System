from database.db_connection import get_db_connection


def search_users(keyword):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    query = """
    SELECT *
    FROM users
    WHERE full_name LIKE %s
       OR email LIKE %s
       OR phone LIKE %s
    ORDER BY id DESC
    """

    search_keyword = f"%{keyword}%"

    cursor.execute(
        query,
        (
            search_keyword,
            search_keyword,
            search_keyword
        )
    )

    users = cursor.fetchall()

    cursor.close()
    connection.close()

    return users