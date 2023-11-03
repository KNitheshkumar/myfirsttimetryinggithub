import pymongo
import json


myclient = pymongo.MongoClient("mongodb://localhost:27017/")


db = myclient.database_sample

collection = myclient.sample_collection

with open('weather_data.json') as file:
    file_data = json.load(file)

collection.insert_one(file_data)