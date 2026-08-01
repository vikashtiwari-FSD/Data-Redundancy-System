from database.db_connection import get_db_connection


def get_dashboard_stats():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)

    stats = {}

    # Total Users
    cursor.execute("SELECT COUNT(*) AS total_users FROM users")
    stats["total_users"] = cursor.fetchone()["total_users"]

    # Total Logs
    cursor.execute("SELECT COUNT(*) AS total_logs FROM submission_logs")
    stats["total_logs"] = cursor.fetchone()["total_logs"]

    # Duplicate Count
    cursor.execute("""
        SELECT COUNT(*) AS duplicates
        FROM submission_logs
        WHERE status='DUPLICATE'
    """)
    stats["duplicates"] = cursor.fetchone()["duplicates"]

    # False Positive Count
    cursor.execute("""
        SELECT COUNT(*) AS false_positive
        FROM submission_logs
        WHERE status='FALSE_POSITIVE'
    """)
    stats["false_positive"] = cursor.fetchone()["false_positive"]

    # Recent Activity
    cursor.execute("""
        SELECT
            full_name,
            email,
            status,
            message,
            submitted_at
        FROM submission_logs
        ORDER BY submitted_at DESC
        LIMIT 10
    """)

    recent_logs = cursor.fetchall()

    cursor.close()
    connection.close()

    return stats, recent_logs