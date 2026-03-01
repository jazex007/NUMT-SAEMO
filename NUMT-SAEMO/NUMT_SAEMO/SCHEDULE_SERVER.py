from flask import jsonify
import pymysql
from NUMT_SAEMO.verify_user import verify
from .verify_user import verify

def get_data():
    conn = pymysql.connect(
        host='jazex007.mysql.pythonanywhere-services.com',
        user='jazex007',
        password='Iwtaplhduewnhxrhpgtrdbeatit',
        database='jazex007$SCHEDULE',
        cursorclass=pymysql.cursors.DictCursor
    )

    with conn.cursor() as cur:
        cur.execute(
            "SELECT time, RA, Dec, url, name FROM observations",
     
        )
        data = cur.fetchall()

    conn.close()

    schedule = []

    for row in data:
        observation = {
            "time": row["time"],
            "RA": row["RA"],
            "Dec": row["Dec"],
            "send-to-url": row["url"],
            "observation-name": row["name"]
        }
        schedule.append(observation)





    return data

def get_schedule_table(clientID, password):
    exists  = verify(clientID, password)
    if exists:
        schedule  = get_data(clientID, password)
    else:
        return jsonify({"error": "Unauthorized clientID"}), 401

    return jsonify(schedule)


def add_observation(conn, time, ra, dec, url, name):
    conn = pymysql.connect(
    host='jazex007.mysql.pythonanywhere-services.com',
    user='jazex007',
    password='Iwtaplhduewnhxrhpgtrdbeatit',
    database='jazex007$SCHEDULE',
    cursorclass=pymysql.cursors.DictCursor
    )
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO observations (time, RA, Dec, url, name)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (time, ra, dec, url, name)
        )
        conn.commit()

