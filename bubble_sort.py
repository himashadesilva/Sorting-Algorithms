from timeit import default_timer as timer
def bubbleSort(a):
    for x in range(len(a) - 1, 0, -1):
        for y in range(x):
            if int(a[y]) > int(a[y + 1]):
                temp = a[y]
                a[y] = a[y + 1]
                a[y+1]=temp
    return a


array = input("Enter elements in one line, separate with ',' : ").split(",")

start = timer()
sorted_array = bubbleSort(array)
end = timer()

print(sorted_array)
print("Elapsed time : ")
print(end - start)
