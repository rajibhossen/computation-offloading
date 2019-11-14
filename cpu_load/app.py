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
def face_recognition(job_id, client_id, start):
    db_conn = database.get_connection()
    cursor = db_conn.cursor()
    
    result = recognize_func()  # face recognition

    end = time.time()
    duration = end - float(start)
    
    cursor.execute("insert into tasks (client_id, job_id, start_time, end_time, duration) values (?,?,?,?,?)",
                   (client_id, job_id, start, end, duration))
    db_conn.commit()
    db_conn.close()
    return "Client: " + str(client_id) + " JOB: " + str(job_id) + " Duration: " + str(duration)


@app.route('/')
def index():
    return "Hello, World"


@app.route('/face_recognition/')
def task_face_recognition():
        
    job_id = request.args.get('job_id')
    client_id = request.args.get('client_id')
    start_time = time.time()
    
    task = face_recognition.delay(job_id, client_id, start_time)
    return str(task)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
