import sys


def mergeSort(A, start, end):
    if start < end:
        middle = (start + end)//2
        mergeSort(A, start, middle)
        mergeSort(A, middle + 1, end)
        merge(A, start, middle, end)
        return A


def merge(A, start, middle, end):
    L = A[start:middle + 1]
    R = A[middle + 1:end + 1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i = j = 0

    for k in range(start, end + 1):

        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1

        else:
            A[k] = R[j]
            j += 1


