from random import randint


original = []
for n in range(0, 10):
    original.append(randint(0, 100))
print(original)

for i in range(1, len(original)):
    if original[i] < original[i - 1]:
        tmp = original[i]
        for k in range(i-1, -1, -1):
            if original[k] <= original[i]:
                if k == 0:
                    original.pop(i)
                    original.insert(1, tmp)
                    break
                else:
                    original.pop(i)
                    original.insert(k+1, tmp)
                    break
        if original.index(tmp) == i:
            original.pop(i)
            original.insert(0, tmp)

print(original)
