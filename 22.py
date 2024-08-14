a = input("Enter your numbers with commas for list 1: \n")
list1 = list(map(int, a.split(",")))

b = input("Enter your numbers with commas for list 2: \n")
list2 = list(map(int, b.split(",")))

inte = []
k1 = list(set(list1))
k2 = list(set(list2))

for i in k1:
    if i in k2:
        inte.append(i)

print(inte)
