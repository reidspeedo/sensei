import pymongo
import os

connection_string = os.environ.get("MONGO_DB_CONN_STR")
client = pymongo.MongoClient(connection_string)
db = client.test

def get_user(username):
    return [{"Name": user['Name'], "Age": user['Age']} for user in db.users.find({"Name": username})]

def get_users():
    return [{"Name": user['Name'],"Age": user['Age']} for user in db.users.find()]

def post_user(user):
    db.users.insert(user)
    return ['Successfully added {} to the database'.format(user["Name"]) for user in db.users.find({"Name": user["Name"]})]

def delete_users(user):
    return {
        "Status": db.users.remove({"Name": user["Name"], "Age": user["Age"]}, True),
        "Details": user
    }
