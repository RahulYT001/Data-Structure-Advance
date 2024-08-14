a = input("Enter the elements with commas:\n")
b = tuple(map(int, a.split(",")))

I1 = int(input("Enter the first index:\n"))
I2 = int(input("Enter the second index:\n"))

l1 = []
for i in range(I1, I2 + 1):
    l1.append(b[i])

a = tuple(l1)
print(a)
