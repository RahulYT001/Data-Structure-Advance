a = input("Enter your strings with commas for set 1: \n")
list1 = list(j.strip() for j in a.split(","))

b = input("Enter your strings with commas for set 2: \n")
list2 = list(k.strip() for k in b.split(","))

set1 = set(list1)
set2 = set(list2)
sym_diff = set1 ^ set2

print(f"The symmetric difference of set 1 and set 2 is, {sym_diff}.")
