from database.db_connection import get_db_connection


def search_users(keyword):

    connection = get_db_connection()

    cursor = connection.cursor(dictionary=True)

    search_keyword = f"%{keyword}%"

    # Search unique users
    user_query = """
    SELECT
        full_name,
        email,
        phone,
        'UNIQUE' AS status,
        'Stored in database' AS message
    FROM users
    WHERE full_name LIKE %s
       OR email LIKE %s
       OR phone LIKE %s
    """

    cursor.execute(
        user_query,
        (
            search_keyword,
            search_keyword,
            search_keyword
        )
    )

    users = cursor.fetchall()

    # Search submission logs
    log_query = """
    SELECT
    full_name,
    email,
    phone,
    status,
    message
FROM submission_logs
WHERE (
    full_name LIKE %s
    OR email LIKE %s
    OR phone LIKE %s
)
AND status <> 'UNIQUE'
ORDER BY id DESC
    """

    cursor.execute(
        log_query,
        (
            search_keyword,
            search_keyword,
            search_keyword
        )
    )

    logs = cursor.fetchall()

    cursor.close()
    connection.close()

    # Merge both lists
    return users + logs