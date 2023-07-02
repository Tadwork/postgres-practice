import psycopg

DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "world-db"
DB_USER = "world"
DB_PASS = "world123"

with  psycopg.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT) as conn:

    with conn.cursor() as cur:
        cur.execute("select count(*) from city")
        row = cur.fetchone()
        print('Count = ', row[0])