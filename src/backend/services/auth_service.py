from models.user import User

# Mock user database
users_db = [User(user_id=1, username="user1", email="user1@example.com", password="password123")]

def authenticate_user(username, password):
    for user in users_db:
        if user.username == username and user.password == password:
            return True
    return False
