import requests
import time
import random
import csv
import os

from multiprocessing import Process
BASE_URL = "http://0.0.0.0:5000"
F_REC = "/face_recognition"


def client_face_recognition(URL, ID):
    poisson_rate = 1 / 3.0  # 1 jobs per 5 sec
    # simulate 30 minutes-10*30 = 300
    begin = time.time()
    time_series = 0
    poisson_data = []
    for i in range(300):
        nextitem = random.expovariate(poisson_rate)
        # time_series += nextitem
        poisson_data.append(nextitem)
        time.sleep(nextitem)

        params = {"job_id": i, "client_id": ID}
        response = requests.get(url=URL, params=params)

        if response.status_code == 200:
            print("[CLIENT %d] JOB-%d submitted" % (ID, i))
        elif response.status_code == 404:
            print("JOB: %d-server error!" % i)

    end = time.time()
    elapsed = end - begin
    print("[CLIENT %d] Simulation Done in %d sec" % (ID, elapsed))

    # y_axis = [1 for i in range(len(poisson_data))]
    # plt.plot(poisson_data, y_axis, 'o-')
    # plt.xlabel('time (s)')
    # filename = "figures/client-" + str(ID) + "-poisson"
    # plt.savefig(filename)
    filename = "generated_data/data-8-10-300-1d2/client-" + str(ID) + "-poisson.csv"
    with open(filename, 'w+') as myfile:
        wr = csv.writer(myfile)
        for val in poisson_data:
            wr.writerow([val])


if __name__ == '__main__':
    # client_face_recognition(BASE_URL + F_REC, 1)
    # client_face_recognition(BASE_URL + F_REC, 2)
    dir = "generated_data/data-8-10-300-1d3/"
    if not os.path.exists(dir):
        os.makedirs(dir)

    jobs = [Process(target=client_face_recognition, args=(BASE_URL + F_REC, i)) for i in range(10)]
    for p in jobs:
        p.start()
    for p in jobs:
        p.join()

    print("All clients done")

