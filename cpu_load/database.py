import sqlite3


def create_table(cur, query):
    cur.execute(query)


def get_connection():
    conn = sqlite3.connect("cpu_load.db")
    return conn


def initialize_db():
    conn = sqlite3.connect("cpu_load.db")
    cursor = conn.cursor()
    sql = 'create table if not exists tasks (id integer primary key, client_id integer, job_id integer, ' \
          'arrival_time timestamp , end_time timestamp, job_time timestamp, queue_time timestamp )'
    cursor.execute(sql)
    conn.commit()
    conn.close()


