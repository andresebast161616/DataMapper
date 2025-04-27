import sqlite3
from models.user import User

class UserMapper:
    def __init__(self, connection):
        self.connection = connection

    def insert(self, user):
        cursor = self.connection.cursor()
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user.name, user.email)
        )
        self.connection.commit()

        user.user_id = cursor.lastrowid

    def find_by_id(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute(
            "SELECT id, name, email FROM users WHERE id = ?",
            (user_id,)
        )
        row = cursor.fetchone()
        if row:
            return User(row[0], row[1], row[2])
        return None
