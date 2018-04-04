from random import randint


def sort(arr, indexL, indexR):
    if indexL < indexR:
        border = partition(arr, indexL, indexR)
        sort(arr, indexL, border-1)
        sort(arr, border, indexR)
    return arr


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
