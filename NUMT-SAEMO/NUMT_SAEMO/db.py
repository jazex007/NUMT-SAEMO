import mysql.connector

def get_connection_NUMT():
    conn = mysql.connector.connect(
        host="jazex007.mysql.pythonanywhere-services.com",
        user="jazex007",
        password="aawv3v34v00700744134##",
        database="jazex007$mydatabase"
    )
    return conn


def get_athing(table, object_id, thing):
    conn = get_connection_NUMT()
    cursor = conn.cursor()

    query = f"SELECT {thing} FROM {table} WHERE id=%s"
    cursor.execute(query, (object_id,))

    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        return result[0]
    return None