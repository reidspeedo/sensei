import pymongo
import os
import logging
from fastapi import HTTPException, status

connection_string = os.environ.get("MONGO_DB_CONN_STR")
client = pymongo.MongoClient(connection_string)
db = client.test

def get_user(username):
    return [{"Name": user['Name'], "Age": user['Age']} for user in db.users.find({"Name": username})]

def get_users():
    return [{"Name": user['Name'],"Age": user['Age']} for user in db.users.find()]

def post_user(user):
    try:
        db.users.insert(user)
        result = [{user["Name"]} for user in db.users.find({"Name": user["Name"]})]
        logging.info( f"Successfully created : {result}")
        return result
    except Exception as e:
        logging.warning(f"Unsucessful save: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to save user.")

def delete_users(user):
    return {
        "Status": db.users.remove({"Name": user["Name"], "Age": user["Age"]}, True),
        "Details": user
    }
