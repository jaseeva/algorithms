from random import randint


original = []
for n in range(0, 10):
    original.append(randint(0, 100))
print(original)

for i in range(0, len(original)-1):
    element = original[i]
    for j in range(i, len(original)):
        if j == len(original)-1:
            if original[j] < original[j-1]:
                original[j], original[j-1] = original[j-1], original[j]
                break
        elif element > original[j+1]:
            element = original[j+1]
        original.pop(original.index(element))
        original.insert(i, element)
print(original)
