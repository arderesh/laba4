from time import perf_counter
from algosi.sorting import insertion_sort


def counter_time_sort(sort_func, values, repaets=5):
    times = []
    for _ in range(repaets):
        data = values.copy()
        start = perf_counter()
        result = sort_func(data)
        elapsed = perf_counter() - start

        times.append(elapsed)
        del result, data

    return times