def intersection(t1,t2):
    inte = []
    k1=list(set(t1))
    k2=list(set(t2))
    for i in k1:
        if i in k2:
            inte.append(i)
    return inte

t1 = (1, 2, 2, 3, 4)
t2 = (2, 2, 4, 6)
intersection = intersection(t1, t2)
print(intersection)