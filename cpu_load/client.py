import requests
import time
import random

import matplotlib.pyplot as plt
from multiprocessing import Process
BASE_URL = "http://0.0.0.0:5000"
F_REC = "/face_recognition"


def client_face_recognition(URL, ID):
    poisson_rate = 1 / 5.0  # 1 jobs per 5 sec
    # simulate 30 minutes-10*30 = 300
    begin = time.time()
    time_series = 0
    poisson_data = []
    for i in range(5):
        nextitem = random.expovariate(poisson_rate)
        time_series += nextitem
        poisson_data.append(time_series)
        time.sleep(nextitem)

        params = {"job_id": i, "client_id": ID}
        response = requests.get(url=URL, params=params)

        if response.status_code == 200:
            print("[CLIENT %d] JOB-%d-submitted" % (ID,i))
        elif response.status_code == 404:
            print("JOB: %d-server error!" % i)

    end = time.time()
    elapsed = end - begin
    print("[CLIENT %d] Simulation Done in %d sec" % (ID, elapsed))
    y_axis = [1 for i in range(len(poisson_data))]
    plt.plot(poisson_data, y_axis, 'o-')
    plt.xlabel('time (s)')
    filename = "figures/client-" + str(ID) + "-poisson"
    plt.savefig(filename)


if __name__ == '__main__':
    client_face_recognition(BASE_URL + F_REC, 1)
    # client_face_recognition(BASE_URL + F_REC, 2)
    # jobs = [Process(target=client_face_recognition, args=(BASE_URL + F_REC, i)) for i in range(8)]
    # for p in jobs:
    #     p.start()
    # for p in jobs:
    #     p.join()

