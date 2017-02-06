from timeit import default_timer as timer
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


array = []
array = input("Enter elements in one line, separate with ',' : ").split(",")

start = timer()
sorted_array = selectionSort(array)
end = timer()

print(sorted_array)
print("Elapsed time : ")
print(end - start)
