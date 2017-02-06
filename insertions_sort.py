from timeit import default_timer as timer
def insertionSort(a):
	for x in range(1,len(a)):
		value = a[x]
		index = x;
		while int(a[index-1])>int(value) and int(index)>0:
			a[index] = a[index-1]
			index = index -1
		a[index]=value
	return a


array = []
array = input("Enter elements in one line, separate with ',' : ").split(",")

start = timer()
sorted_array = insertionSort(array)
end = timer()

print(sorted_array)
print("Elapsed time : ")
print(end - start)