import time
import re
import subprocess
import csv

cmd = "redis-cli -n DATABASE_NUMBER llen celery"
filename = "generated_data/data-8-10-300-1d3/queue_length.csv"

for i in range(600):
    data = subprocess.call(cmd, shell=True)
    data = str(data)
    length = int(re.search(r'\d+', data).group())
    t = time.time()
    with open(filename, 'w+') as myfile:
        wr = csv.writer(myfile)
        wr.writerow([t, length])
    time.sleep(2)
