import pymongo
import os

connection_string = os.environ.get("MONGO_DB_CONN_STR")
client = pymongo.MongoClient(connection_string)
db = client.test
users = []

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
    result = []
    for user in db.users.find():
        result.append({
            "Name": user['Name'],
            "Age": user['Age']
        })

        print(user)
    return result

def post_user(user):
    users.append(user)
    db.users.insert(user)
    #return users
