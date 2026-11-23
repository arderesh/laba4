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
