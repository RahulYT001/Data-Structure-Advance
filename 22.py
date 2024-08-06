def intersection(l1,l2):
    inte = []
    k1=list(set(l1))
    k2=list(set(l2))
    for i in k1:
        if i in k2:
            inte.append(i)
    return inte

a = input("Enter your numbers with commas for list 1: \n")
list1 = list(map(int, a.split(",")))

b = input("Enter your numbers with commas for list 2: \n")
list2 = list(map(int, b.split(",")))

intersection = intersection(list1, list2)
print(intersection)