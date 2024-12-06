import unittest
from StringUtils import StringUtils

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    def test_reverse_string(self):
        self.assertEqual(self.utils.reverse_string("arara"), "arara")
        self.assertEqual(self.utils.reverse_string("python"), "nohtyp")
        self.assertEqual(self.utils.reverse_string(""), "")

    def test_is_palindrome(self):
        self.assertTrue(self.utils.is_palindrome("arara"))
        self.assertTrue(self.utils.is_palindrome("madam"))
        self.assertFalse(self.utils.is_palindrome("python"))

if __name__ == "__main__":
    unittest.main()
