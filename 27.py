a = input("Enter the elements with commas:\n")
b=tuple(map(int, a.split(",")))

lowest = b[0]
greatest = b[0]
for i in b:
    if i < lowest:
        lowest = i
for k in b:
    if k>greatest:
        greatest = k

print(f"The max value in this tuple is: {greatest}")
print(f"The min value in this tuple is: {lowest}")