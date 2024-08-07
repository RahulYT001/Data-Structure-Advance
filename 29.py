a = input("Enter the elements with commas:\n")
b=tuple(a.split(","))
ele = input("Enter the element: \n")

c=0
for i in b:
    if i == ele:
        c+=1
print(f"The number of occurencies of {ele} in {b} is {c}.")