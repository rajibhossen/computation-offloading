from pymongo import MongoClient
import csv

DATA_DIR = "generated_data/data-64-20-400-1d3/"


client = MongoClient('localhost', 27017)
db = client['cpu_load']

collection = db.posts

filename = DATA_DIR + "data-64-20-400-1d3.csv"
with open(filename, 'w+') as myfile:
    wr = csv.writer(myfile)
    for doc in collection.find():
        wr.writerow([doc])

x = collection.delete_many({})
print(x.deleted_count, " documents deleted.")


