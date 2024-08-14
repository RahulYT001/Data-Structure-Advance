list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 4, 6]
inte = []
k1 = list(set(list1))
k2 = list(set(list2))

for i in k1:
    if i in k2:
        inte.append(i)

print(inte)
