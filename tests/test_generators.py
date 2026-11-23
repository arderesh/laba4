from unittest import TestCase
from algosi.generators import random_values, sorted_values, reverse_values, pochti_sorted_values, duplicate_values


class TestGenerators(TestCase):
    def test_emty(self):
        self.assertEqual(random_values(0), [])
        self.assertEqual(sorted_values(0), [])
        self.assertEqual(reverse_values(0), [])
        self.assertEqual(pochti_sorted_values(0), [])
        self.assertEqual(duplicate_values(0), [])

    def test_sort_and_rev(self):
        self.assertEqual(sorted_values(4), [0, 1, 2, 3])
        self.assertEqual(reverse_values(4), [3, 2, 1, 0])

    def test_random(self):
        values = random_values(20, seed=17)
        self.assertEqual(len(values), 20)
        self.assertTrue(all(-20 <= value <= 20 for value in values))

    def test_pochti_sorted_vals(self):
        values = pochti_sorted_values(10, seed=17)
        self.assertEqual(sorted(values), list(range(10)))
        changed_positions = sum(value != index for index, value in enumerate(values))
        self.assertEqual(changed_positions, 2)

    def test_duplicates(self):
        values = duplicate_values(20, seed=17)

        self.assertEqual(len(values), 20)
        self.assertTrue(all(0 <= value <= 9 for value in values))
        self.assertLess(len(set(values)), len(values))

    def test_seed(self):
        for generate in (random_values, pochti_sorted_values, duplicate_values):
            with self.subTest(generator=generate.__name__):
                first = generate(250, seed=17)
                same_seed = generate(250, seed=17)
                other_seed = generate(250, seed=18)

                self.assertEqual(first, same_seed)
                self.assertNotEqual(first, other_seed)