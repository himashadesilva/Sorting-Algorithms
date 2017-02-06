def bubbleSort(a):
    for x in range(len(a) - 1, 0, -1):
        for y in range(x):
            if int(a[y]) > int(a[y + 1]):
                temp = a[y]
                a[y] = a[y + 1]
                a[y+1]=temp
    return a


def selectionSort(a):
    for x in range(len(a) - 1, 0, -1):
        indexOfMax = 0
        for y in range(1, x + 1):
            if int(a[y]) > int(a[indexOfMax]):
                indexOfMax = y

        temp = a[x]
        a[x] = a[indexOfMax]
        a[indexOfMax] = temp

    return a


def insertionSort(a):
    for x in range(1, len(a)):
        value = a[x]
        index = x;
        while int(a[index - 1]) > int(value) and int(index) > 0:
            a[index] = a[index - 1]
            index = index - 1
        a[index] = value
    return a

