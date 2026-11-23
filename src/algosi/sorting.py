def insertion_sort(vals):
    copy_val = vals.copy()
    for i in range(1, len(copy_val)):
        value = copy_val[i]
        j = i - 1

        while j >= 0 and value < copy_val[j]:
            copy_val[j + 1] = copy_val[j]
            j -= 1
        copy_val[j + 1] = value

    return copy_val

def fast_sort(vals):
    if len(vals) <= 1:
        copy_vals = vals.copy()
        return copy_vals
    mediana = vals[len(vals) // 2]

    smoller = []
    equal = []
    bigger = []

    for value in vals:
        if value < mediana:
            smoller.append(value)
        elif value == mediana:
            equal.append(value)
        elif value > mediana:
            bigger.append(value)

    return fast_sort(smoller) + equal + fast_sort(bigger)