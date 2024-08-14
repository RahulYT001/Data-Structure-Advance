l = [1, 1, 23, 45, 56, 23]

set = set()
result = []

for i in l:
    if i not in set:
        result.append(i)
        set.add(i)

print(result)
