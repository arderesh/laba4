from time import perf_counter
from algosi.sorting import insertion_sort, fast_sort
from algosi.generators import (random_values, sorted_values, reverse_values,
                               pochti_sorted_values, duplicate_values)
import csv
from statistics import median

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


def run_benchmark(output_path="bench_res.csv"):
    sizes = [100_000, 1_000_000, 10_000_000]

    sorts = [("insertion_sort", insertion_sort), ("fast_sort", fast_sort)]

    generators = [("random", random_values, True), ("sorted", sorted_values, False),
                  ("reverse", reverse_values, False),
                  ("pochti_sorted", pochti_sorted_values, True),
                  ("duplicates", duplicate_values, True)]

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["sort", "input_type", "size", "repeats",
                         "median_seconds", "status"])

        for size in sizes:
            for input_type, generate, use_seed in generators:
                if use_seed:
                    values = generate(size, seed=17)
                else:
                    values = generate(size)
                for sort_name, sort_func in sorts:
                    if sort_func is insertion_sort and input_type in {"random", "reverse", "duplicates"}:
                        writer.writerow([sort_name, input_type, size, 0, "", "skipped"])
                        continue
                    times = counter_time_sort(sort_func, values)
                    writer.writerow([sort_name, input_type, size, len(times), median(times), "okey"])

                del values


if __name__ == "__main__":
    run_benchmark()