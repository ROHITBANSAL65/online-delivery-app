from datetime import datetime

class User:
    def __init__(self, user_id, username, email, password, created_at=None):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = created_at if created_at else datetime.utcnow()
