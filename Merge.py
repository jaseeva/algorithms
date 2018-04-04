from random import randint


original = []
for n in range(0, 10):
    original.append(randint(0, 100))
print(original)


def divide(arr):
    arr1 = []
    arr2 = []
    if len(arr) <= 1:
        return

    for i in range(0, int(len(arr)/2)):
        arr1.append(arr[i])
    for i in range(int(len(arr) / 2), len(arr)):
        arr2.append(arr[i])

    divide(arr1)
    divide(arr2)
    merge(arr, arr1, arr2)


def merge(arr, arrL, arrR):
    indexO = 0
    indexL = 0
    indexR = 0

    while indexO < len(arr):
        if indexL >= len(arrL):
            arr[indexO] = arrR[indexR]
            indexR += 1
        elif indexR >= len(arrR):
            arr[indexO] = arrL[indexL]
            indexL += 1
        elif arrL[indexL] <= arrR[indexR]:
            arr[indexO] = arrL[indexL]
            indexL += 1
        else:
            arr[indexO] = arrR[indexR]
            indexR += 1

        indexO += 1


divide(original)
print(original)
