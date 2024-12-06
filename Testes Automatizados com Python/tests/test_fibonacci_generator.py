import unittest
from FibonacciGenerator import FibonacciGenerator

class TestFibonacciGenerator(unittest.TestCase):
    def setUp(self):
        self.generator = FibonacciGenerator()

    def test_generate_sequence(self):
        self.assertEqual(self.generator.generate_sequence(5), [0, 1, 1, 2, 3])
        self.assertEqual(self.generator.generate_sequence(0), [])
        self.assertEqual(self.generator.generate_sequence(-1), [])

    def test_get_nth_number(self):
        self.assertEqual(self.generator.get_nth_number(1), 0)
        self.assertEqual(self.generator.get_nth_number(2), 1)
        self.assertEqual(self.generator.get_nth_number(5), 3)
        self.assertIsNone(self.generator.get_nth_number(-1))

if __name__ == "__main__":
    unittest.main()
