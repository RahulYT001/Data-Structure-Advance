v = "AEIOUaeiou"
count = 0
for k in (a := input("Enter the string\n")):    
    if k in v:
        count += 1
print(count)
