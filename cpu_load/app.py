import time

from celery import Celery
from flask import Flask, request
from datetime import datetime

from recognize_faces import recognize_func

app = Flask(__name__)

celery = Celery(broker='redis://localhost:6379/0')


@celery.task(name='face.recognition')
def face_recognition(job_id, client_id, start):
    result = recognize_func()  # face recognition

    end = time.time()
    duration = end - float(start)
    return "Client ID: " + str(client_id) + " JOB ID: " + str(job_id) + " Start: " + \
           str(start) + " Duration: " + str(duration)


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
