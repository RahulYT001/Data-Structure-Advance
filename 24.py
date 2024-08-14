a = input("Enter your strings with commas for set 1: \n")
set1 = set(s.strip() for s in a.split(","))

b = input("Enter your strings with commas for set 2: \n")
set2 = set(s.strip() for s in b.split(","))

difference = set1 - set2

print(difference)
