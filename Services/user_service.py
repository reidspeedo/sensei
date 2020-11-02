from repository import users_repository


def get_user(username):
    return users_repository.get_user(username)

def get_users():
    return users_repository.get_users()

def post_user(username):
    return users_repository.post_user(username)