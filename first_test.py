import unittest

def sum_two(a, b):
    return a + b

class MainTest(unittest.TestCase):
    def test_hello(self):
        print("Hello from the tests")

    def test_sum_two(self):
        returned_value = sum_two(5,7)
        self.assertEqual(returned_value, 12)
        self.assertEqual(sum_two(-5,5), 0)
