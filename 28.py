def intersection(l1,l2):
    set1=set(l1)
    set2=set(l2)
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)

    return f"The union is {union}, intersection is {intersection} and difference is {difference}."




a = input("Enter your numbers with commas for set 1: \n")
list1 = list(map(int, a.split(",")))

b = input("Enter your numbers with commas for set 2: \n")
list2 = list(map(int, b.split(",")))

print(intersection(list1, list2))