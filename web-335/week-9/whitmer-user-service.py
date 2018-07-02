from pymongo import MongoClient
import pprint
import datetime

client = MongoClient('localhost', 27017)
db = client.web335

user = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@mail.com",
    "employee_id": "42",
    "date_created": datetime.datetime.utcnow()
}

user_id = db.users.insert_one(user).inserted_id

print(user_id)

pprint.pprint(db.users.find_one({"email": "johndoe@mail.com"}))