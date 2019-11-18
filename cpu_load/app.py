import time
import sqlite3
from celery import Celery
from flask import Flask, request
from datetime import datetime

import database
from recognize_faces import recognize_func

app = Flask(__name__)

celery = Celery(broker='redis://localhost:6379/0')

database.initialize_db() # initializing db connection


@celery.task(name="face.recognition")
def face_recognition(job_id, client_id, queue_start):
    queue_end = time.time()
    queue_duration = queue_end - queue_start
    start = time.time()
    
    result = recognize_func()  # face recognition

    end = time.time()
    duration = end - float(start)
    total = queue_duration + duration
    db_conn = database.get_connection()
    cursor = db_conn.cursor()
    count = 0
    while True:
        try:
            cursor.execute("insert into tasks (client_id, job_id, arrival_time, end_time, job_time, queue_time,total_time) "
                   "values (?,?,?,?,?,?,?)", (client_id, job_id, queue_start, end, duration, 
                                              queue_duration, total))
            db_conn.commit()
        except sqlite3.Error as e:
            print("write failed, trying again")
            count += 1
            if count == 5:
                db_conn.close()
                break
            continue
        db_conn.close()
        break

    return "Client: " + str(client_id) + " JOB: " + str(job_id) + " Total: " + str(duration+queue_duration)


@app.route('/')
def index():
    return "Hello, World"


@app.route('/face_recognition/')
def task_face_recognition():
        
    job_id = request.args.get('job_id')
    client_id = request.args.get('client_id')
    queue_time = time.time()
    
    task = face_recognition.delay(job_id, client_id, queue_time)
    return str(task)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
