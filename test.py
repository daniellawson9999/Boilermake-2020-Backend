import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["mydatabase"]

dblist = client.list_database_names()

if "mydatabase" in dblist:
    print('yes')
