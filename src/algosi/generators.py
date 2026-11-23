import random

def random_values(size, seed=None):
    rnge = random.Random(seed)

    values = []
    for _ in range(size):
        values.append(rnge.randint(-size, size))

    return values


def sorted_values(size):
    res = []
    for i in range(0, size):
        res.append(i)

    return res


def reverse_values(size):
    res = []
    for i in range(size - 1, -1, -1):
        res.append(i)

    return res


def pochti_sorted_values(size, seed=None):
    lst = sorted_values(size)

    if size < 2:
        return lst

    rnge = random.Random(seed)
    swaps = max(1, size // 100)
    pairs = rnge.sample(range(size // 2), swaps)

    for pair in pairs:
        left = 2 * pair

        lst[left], lst[left + 1] = lst[left + 1], lst[left]

    return lst


def duplicate_values(size, seed=None):
    rnge = random.Random(seed)
    values = []

    for _ in range(size):
        values.append(rnge.randint(0, 9))

    return values