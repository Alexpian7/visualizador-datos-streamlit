import pymongo
import pandas as pd
from pymongo import MongoClient

client = MongoClient()

client = MongoClient('mongodb+srv://') #conexión mongodb
db = client["dbTest"]
collection = db["user"]

cursor = collection.find()
for document in cursor:
    print(document)

df = pd.DataFrame(list(collection.find()))
print(df)