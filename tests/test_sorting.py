from random import Random
from unittest import TestCase

from algosi.sorting import fast_sort, insertion_sort


class TestSorting(TestCase):
    def test_edge_cases(self):
        cases = (("empty", [], []), ("single", [5], [5]),
                 ("sorted", [1, 2, 3], [1, 2, 3]), ("reverse", [3, 2, 1], [1, 2, 3]),
                 ("duplicates", [3, 1, 3, 2, 1], [1, 1, 2, 3, 3]),
                 ("negatives", [-2, 0, -5, 3], [-5, -2, 0, 3]))

        for sort in (insertion_sort, fast_sort):
            for name, values, expect in cases:
                with self.subTest(sort=sort.__name__, case=name):
                    data = values.copy()
                    result = sort(data)

                    self.assertEqual(result, expect)
                    self.assertEqual(data, values)
                    self.assertIsNot(result, data)

    def test_random_lists_match_sorted(self):
        rnge = Random(17)

        for size in (8, 32, 128):
            values = [rnge.randint(-20, 20) for _ in range(size)]
            expect = sorted(values)

            for sort in (insertion_sort, fast_sort):
                with self.subTest(sort=sort.__name__, size=size):
                    self.assertEqual(sort(values.copy()), expect)

    def test_fast_sort_on_large_ordered_lists(self):
        expect = list(range(5_000))

        self.assertEqual(fast_sort(expect.copy()), expect)
        self.assertEqual(fast_sort(expect[::-1]), expect)
