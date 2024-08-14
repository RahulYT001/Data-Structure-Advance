a = input("Enter your strings with commas: \n")
list1 = list(j.strip() for j in a.split(","))
set1 = set(list1)
d = {item: 0 for item in set1}

for item in list1:
    if item in d:
        d[item] += 1

print(d.items())
