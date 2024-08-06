def intersection(l1,l2):
    inte = []
    k1=list(set(l1))
    k2=list(set(l2))
    for i in k1:
        if i in k2:
            inte.append(i)
    return inte

list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 4, 6]
intersection = intersection(list1, list2)
print(intersection)