import sqlite3
from sqlite3 import Error


def create_table(cur, query):
    cur.execute(query)


def get_connection():
    connection = None
    try:
        connection = sqlite3.connect("cpu_load.db")
    except Error as e:
        print(e)

    cursor = connection.cursor()

    sql_create_tasks_table = """CREATE TABLE IF NOT EXISTS tasks (
                                        client_id integer PRIMARY KEY,
                                        job_id integer NOT NULL,
                                        start_time timestamp NOT NULL,
                                        end_time timestamp NOT NULL,
                                        duration timestamp NOT NULL 
                                    );"""

    create_table(cursor, sql_create_tasks_table)

    return cursor


def close_connection(connection):
    connection.close()

