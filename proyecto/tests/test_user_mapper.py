import unittest
import sqlite3
from models.user import User
from mappers.user_mapper import UserMapper

class TestUserMapper(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.connection = sqlite3.connect(':memory:')
        cursor = cls.connection.cursor()
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT)")
        cls.connection.commit()
        cls.mapper = UserMapper(cls.connection)

    @classmethod
    def tearDownClass(cls):
        cls.connection.close()

    def test_insert_user(self):
        new_user = User(1, "John Doe", "john.doe@example.com")
        
        self.mapper.insert(new_user)

        cursor = self.connection.cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id=?", (new_user.user_id,))
        row = cursor.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row[0], new_user.user_id)
        self.assertEqual(row[1], new_user.name)
        self.assertEqual(row[2], new_user.email)

    def test_find_by_id(self):
        new_user = User(1, "Jane Doe", "jane.doe@example.com")
        
        self.mapper.insert(new_user)

        retrieved_user = self.mapper.find_by_id(1)
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.user_id, new_user.user_id)
        self.assertEqual(retrieved_user.name, new_user.name)
        self.assertEqual(retrieved_user.email, new_user.email)

    def test_find_non_existent_user(self):
        retrieved_user = self.mapper.find_by_id(999)
        self.assertIsNone(retrieved_user)

if __name__ == '__main__':
    unittest.main()