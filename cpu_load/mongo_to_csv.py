from pymongo import MongoClient
import csv

FILEDIR = "data-64-20-300-1d7"
DATA_DIR = "generated_data/" + FILEDIR + "/" 

client = MongoClient('localhost', 27017)
db = client['cpu_load']

collection = db.tasks

filename = DATA_DIR + FILEDIR + ".csv"
headers = ["client_id", "job_id", "arrival_time", "end_time", "job_time", "queue_time", "total_time"]

with open(filename, 'w+') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(headers)
    for doc in collection.find():
        data = [doc['client_id'], doc['job_id'], doc['arrival_time'], doc['end_time'], 
                doc['job_time'], doc['queue_time'], doc['total_time']]
        wr.writerow(data)

x = collection.delete_many({})
print(x.deleted_count, " documents deleted.")


