import psycopg2
from config import config

def edit(r_name, r_phone_number):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute('call edit(%s, %s)', (r_name, r_phone_number))
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()

edit('Papa', '87787970000')
edit('Apa', '87010260006')