list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 4, 6]

k1 = list(set(list1))
k2 = list(set(list2))

if len(k1) > len(k2):
    longer_list = k1
else:
    longer_list = k2

union = []

if longer_list == k1:
    for i in k1:
        if i not in k2:
            union.append(i)
else:
    for i in k2:
        if i not in k1:
            union.append(i)

for i in (k1 if longer_list == k2 else k2):
    if i not in union:
        union.append(i)

print(union)
