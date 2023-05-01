data = [('Askar', '87023981619'), ('Nur', '87788694524'), ('Jamal', '87779985234')]

import psycopg2
from config import config

def check(object):
    list = []
    cnt = -1
    for i in object:
        cnt += 1
        if not i[1].isdigit():
            del object[cnt]
    return object

def insert_list(object):
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.executemany('call insert_list(%s, %s)', object)
        conn.commit()
        cur.close()
    except Exception as e:
        print(str(e))
    finally:
        if conn is not None:
            conn.close()
            
insert_list(data)