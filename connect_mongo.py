import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['employee']
collection = db['attendance']

def insert_data(id, name, date, time):
    data = {'id':id,'name':name, 'date': date, 'time': time }
    cursor = collection.insert_one(data)
    if(cursor):print("INSERTED")

def fetch_all():
    docs = collection.find()
    return docs

def fetch_by_date(date):
    cursor = collection.find({'date': date})
    return cursor

def fetch_by_id(id):
    id = int(id)
    cursor = collection.find({'id':id})
    return cursor

def fetch_by_IdDate(id, date):
    id = int(id)
    cursor = collection.find({'id':id, 'date':date})
    return cursor

