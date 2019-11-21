import requests
import time
import random
import csv
import os

from multiprocessing import Process
BASE_URL = "http://0.0.0.0:5000"
F_REC = "/face_recognition"
DATA_DIR = "generated_data/data-64-20-300-1d7/"
CLIENTS = 20
POISSON_RATE = 1/7.0

def client_face_recognition(URL, ID):
    # simulate 30 minutes-10*30 = 300
    begin = time.time()
    time_series = 0
    poisson_data = []
    for i in range(300):
        nextitem = random.expovariate(POISSON_RATE)
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
    filename = DATA_DIR + "client-" + str(ID) + "-poisson.csv"
    with open(filename, 'w+') as myfile:
        wr = csv.writer(myfile)
        for val in poisson_data:
            wr.writerow([val])
        wr.writerow([elapsed])


if __name__ == '__main__':
    # client_face_recognition(BASE_URL + F_REC, 1)
    # client_face_recognition(BASE_URL + F_REC, 2)
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    jobs = [Process(target=client_face_recognition, args=(BASE_URL + F_REC, i)) for i in range(CLIENTS)]
    for p in jobs:
        p.start()
    for p in jobs:
        p.join()

    print("All clients done")

