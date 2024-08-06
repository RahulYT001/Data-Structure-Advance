
a=input("Enter 1st set of strings with commas in between\n")
b=input("Enter 2nd set of strings with commas in between\n")

l1 = [s.strip() for s in a.split(",")]
l2 = [k.strip() for k in b.split(",")]

for i in l1:
    if i not in l2:
        print(i)