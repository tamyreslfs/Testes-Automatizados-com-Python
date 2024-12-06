import unittest
from UserManager import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.manager = UserManager()

    def test_add_user(self):
        self.assertIsNone(self.manager.add_user("Alice"))
        self.assertIsNone(self.manager.add_user("Bob"))
        self.assertEqual(self.manager.add_user("Alice"), "User already exists")

    def test_remove_user(self):
        self.manager.add_user("Alice")
        self.assertEqual(self.manager.remove_user("Alice"), "User Alice removed successfully")
        self.assertEqual(self.manager.remove_user("Charlie"), "User Charlie not found")

    def test_users_list(self):
        self.manager.add_user("Alice")
        self.manager.add_user("Bob")
        self.assertEqual(self.manager.users, ["Alice", "Bob"])

if __name__ == "__main__":
    unittest.main()
