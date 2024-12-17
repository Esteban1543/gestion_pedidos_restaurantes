from django.db import connection


def get_report_restaurants_by_id(params: list) -> list:
    query = """
        SELECT
            r.name as restaurant,
            COUNT(o.id) as orders,
            SUM(o.total_amount) AS total_amount
        FROM orders o
        INNER JOIN restaurants r ON o.restaurants_id = r.id
        WHERE r.id = %s AND o.created_at BETWEEN %s AND %s
        GROUP BY r.name;
    """
    with connection.cursor() as cursor:
        cursor.execute(query, params)
        if cursor.description:
            columns: list = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        return []
