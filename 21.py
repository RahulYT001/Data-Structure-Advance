t1 = (1, 2, 2, 3, 4)
t2 = (2, 2, 4, 6)
inte = []
k1 = list(set(t1))
k2 = list(set(t2))

for i in k1:
    if i in k2:
        inte.append(i)

print(inte)
