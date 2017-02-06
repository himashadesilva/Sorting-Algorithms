def partition(array, start, end):
    pivot = array[end]
    i = start
    j = start

    while j <= (end - 1):
        if array[j] <= pivot:
            # swap n[i] and n[j] and increment i
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1

        j += 1

    # At the end, n[i] will hold a value larger than pivot

    temp = array[i]
    array[i] = pivot
    array[end] = temp

    return i


def quickSort(array, start, end):
    if start < end:
        pivot = partition(array, start, end)

        quickSort(array, start, pivot - 1)
        quickSort(array, pivot + 1, end)

    return array
