from random import randint


original = []
for n in range(0, 10):
    original.append(randint(0, 100))
print(original)


def sort(arr, indexL, indexR):
    if indexL < indexR:
        border = partition(arr, indexL, indexR)
        sort(arr, indexL, border-1)
        sort(arr, border, indexR)


def partition(arr, i, j):
    indexL = i
    indexR = j
    pivotIndex = randint(indexL, indexR)
    pivotValue = arr[pivotIndex]

    while indexL <= indexR:
        while arr[indexL] < pivotValue:
            indexL += 1
        while arr[indexR] > pivotValue:
            indexR -= 1
        if indexL <= indexR:
            arr[indexL], arr[indexR] = arr[indexR], arr[indexL]
            indexL += 1
            indexR -= 1
    return indexL


sort(original, 0, len(original)-1)
print(original)
