def count_ways_iterative(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError('Тип числа должен быть int')
    if n < 0:
        raise ValueError('Число должно быть >= 0')

    first, second = 1, 1
    if n == 0 or n == 1:
        return 1

    for i in range(2, n + 1):
        res = first + second
        first, second = second, res
    return second


def count_ways_recursive(n):
    if isinstance(n, bool) or not isinstance(n, int):
        raise TypeError('Тип числа должен быть int')
    if n < 0:
        raise ValueError('Число должно быть >= 0')

    if n == 0 or n == 1:
        return 1

    return count_ways_recursive(n - 1) + count_ways_recursive(n - 2)