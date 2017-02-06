from timeit import default_timer as timer
from random import randint

from algorithms import bubbleSort, selectionSort, insertionSort

elements = input("Enter no of elements, (array will generate automatically) : ")
array = []

for x in range(0,int(elements)):
    array.append(randint(-500,1000))

print("array : \n",array)


start = timer()
sorted_array = bubbleSort(array)
end = timer()

print("Sorted array : \n",sorted_array)
bubbleSort_time = end - start
print("elapsed time for bubble sort :", bubbleSort_time)

start = timer()
sorted_array = selectionSort(array)
end = timer()
selectionSort_time = end - start
print("elapsed time for selection sort :", selectionSort_time)

start = timer()
sorted_array = insertionSort(array)
end = timer()
insertionSort_time = end - start
print("elapsed time for insertion sort :", insertionSort_time)
