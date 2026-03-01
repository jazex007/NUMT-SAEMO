import pymysql


def verify(clientID, password):
    conn = pymysql.connect(
        host='jazex007.mysql.pythonanywhere-services.com',
        user='jazex007',
        password='Iwtaplhduewnhxrhpgtrdbeatit',
        database='jazex007$NUMT-SAEMO_clients',
        cursorclass=pymysql.cursors.DictCursor
    )

    with conn.cursor() as cur:
        cur.execute(
         """
          SELECT EXISTS(
               SELECT 1
                FROM users
               WHERE clientID = %s
                AND password = %s
           ) AS user_exists
         """,
          (clientID, password)
     )

    exists = cur.fetchone()['user_exists']

        




    return exists

