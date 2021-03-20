import unittest
def min(l):
    # Should find and return minimum value in a given list
    min = l[0]
    for val in l:
        if val < min:
            min = val
    return min
def sum_list(l):
    # Should return total value of all list items
    total = 0
    for val in l:
        total += val
    return total
def less_than(a):
    # Should return a bool of whether given value is less than 100
    return a < 100
### For this exercise, work within this class. This is something you will come up with on your own soon ###
class MainTest(unittest.TestCase):
    # tests go here!
    def test_min(self):
        self.assertIs(min([1,2,3]), 1)
        self.assertIs(min([3,2,1]), 1)
        self.assertIs(min([100,3,45,4]),3)

    def test_sum_list(self):
        self.assertEqual(sum_list([10,80,5,5]),100)
        self.assertEqual(sum_list([100,20,30]),150)
        self.assertEqual(sum_list([17,3,20]),40)

    def test_less_than(self):
        self.assertTrue(less_than(5))
        self.assertTrue(less_than(55))
        self.assertTrue(less_than(99))
        self.assertFalse(less_than(101))
        self.assertFalse(less_than(201))
        self.assertFalse(less_than(171))
