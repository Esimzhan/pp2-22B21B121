import psycopg2
from config import config

def pattern():
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.callproc('pattern', ())
        row = cur.fetchone()
        while row is not None:
            print(*row)
            row = cur.fetchone()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

pattern()