def intersection(l1,l2):
    set1=set(l1)
    set2=set(l2)
    return set1 ^ set2

a = input("Enter your strings with commas for set 1: \n")
list1 = list(j.strip() for j in a.split(","))

b = input("Enter your strings with commas for set 2: \n")
list2 = list(k.strip() for k in b.split(","))

print(f"The symetric difference of set 1 and set 2 is, {intersection(list1, list2)}.")