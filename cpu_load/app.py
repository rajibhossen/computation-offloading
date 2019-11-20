import time
import sqlite3
from celery import Celery
from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

import database
from recognize_faces import recognize_func

app = Flask(__name__)

celery = Celery(broker='redis://localhost:6379/0')

# database.initialize_db() # initializing db connection


@celery.task(name="face.recognition")
def face_recognition(job_id, client_id, queue_start):
    queue_end = time.time()
    queue_duration = queue_end - queue_start
    start = time.time()
    
    result = recognize_func()  # face recognition

    end = time.time()
    duration = end - float(start)
    total = queue_duration + duration

    # client = MongoClient("localhost", 27017)
    # db = client["cpu_load"]
    # table = db.tasks
    # db_conn = database.get_connection()
    # cursor = db_conn.cursor()
    # count = 0

    data = {"client_id": client_id,
            "job_id": job_id,
            "arrival_time": queue_start,
            "end_time": end,
            "job_time": duration,
            "queue_time": queue_duration,
            "total_time": total}
    with MongoClient("localhost", 27017) as connection:
        db = connection.cpu_load
        db.tasks.insert_one(data)
    return "Client#JOB: " + str(client_id) + "#" + str(job_id) + " Total: " + str(duration+queue_duration)


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
