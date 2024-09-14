from .models.user import User

def get_users():
    return [User(username="user1", email="user1@example.com", is_active=True)]
