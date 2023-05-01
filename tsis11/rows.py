import psycopg2
from config import config

def getrows(pagenumber, pagesize):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('select * from getrows(%s, %s)', (pagenumber, pagesize))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

getrows(1, 2)