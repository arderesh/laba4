from unittest import TestCase
from algosi.stairs import count_ways_iterative, count_ways_recursive

class TestStairs(TestCase):
    def test_zero(self):
        self.assertEqual(count_ways_iterative(0), 1)
        self.assertEqual(count_ways_recursive(0), 1)

    def test_one(self):
        self.assertEqual(count_ways_iterative(1), 1)
        self.assertEqual(count_ways_recursive(1), 1)

    def test_correct_steps(self):
        self.assertEqual(count_ways_iterative(2), 2)
        self.assertEqual(count_ways_recursive(2), 2)

        self.assertEqual(count_ways_iterative(4), 5)
        self.assertEqual(count_ways_recursive(4), 5)

    def test_negative(self):
        self.assertRaises(ValueError, count_ways_iterative, -1)
        self.assertRaises(ValueError, count_ways_recursive, -1)

    def test_non_integer(self):
        self.assertRaises(TypeError, count_ways_iterative, True)
        self.assertRaises(TypeError, count_ways_recursive, True)

        self.assertRaises(TypeError, count_ways_iterative, "2")
        self.assertRaises(TypeError, count_ways_recursive, "2")

        self.assertRaises(TypeError, count_ways_iterative, 2.3)
        self.assertRaises(TypeError, count_ways_recursive, 7.2)