from fastapi import FastAPI, status
import uvicorn
from pydantic import BaseModel
from Services import user_service

app = FastAPI()

class User(BaseModel):
    Name: str
    Age: int


@app.get("/users/{username}")
def get_users(username):
    return user_service.get_user(username)

@app.get("/users")
def all_users():
    return user_service.get_users()


@app.post("/users", status_code=status.HTTP_201_CREATED)
def post_user(user: User):
    return user_service.post_user(dict(user))

if __name__ == '__main__':
    uvicorn.run("app:app", host ='127.0.0.1', port=5000)
