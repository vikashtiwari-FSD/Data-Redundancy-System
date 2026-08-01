from database.db_connection import get_db_connection


def save_log(full_name, email, phone, status, message):

    connection = get_db_connection()

    cursor = connection.cursor()

    query = """
    INSERT INTO submission_logs
    (full_name, email, phone, status, message)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        full_name,
        email,
        phone,
        status,
        message
    )

    cursor.execute(query, values)

    connection.commit()

    cursor.close()
    connection.close()