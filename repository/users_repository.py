import pymongo
import os

connection_string = os.environ.get("MONGO_DB_CONN_STR")
client = pymongo.MongoClient(connection_string)
db = client.test

def get_user(username):
    if username == 'Reid':
        return {
            'Name':'Reid',
            'Age':'27'
        }
    if username == 'Nardo':
        return {
            'Name':'Reid',
            'Age':'31'
        }
    else:
        return{
            'Name': 'Unknown',
            'Age': 'Unknown'
        }

def get_users():
    return [{"Name": user['Name'],"Age": user['Age']} for user in db.users.find()]

def post_user(user):
    db.users.insert(user)
    return print('User: {} has been added to the user collection'.format(db.users.find({"Name": user["Name"]})))

