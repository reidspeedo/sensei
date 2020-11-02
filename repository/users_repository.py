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
    return users

def post_user(user):
    users.append(user)
    return users

