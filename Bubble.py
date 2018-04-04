from random import randint


original = []
for i in range(0, 10):
    original.append(randint(0, 100))
print(original)


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]
    return arr[left], arr[right]


swapped = True

while swapped:
    swapped = False
    for k in range(0, len(original) - 1):
        if original[k] > original[k+1]:
            original[k], original[k+1] = swap(original, k, k+1)
            swapped = True
print(original)
