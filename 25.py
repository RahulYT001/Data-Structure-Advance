def new_tuple(b,I1,I2):
    l1= []
    for i in range(I1,I2+1):
        l1.append(b[i])
    return tuple(l1)


a = input("Enter the elements with commas:\n")
b=tuple(map(int, a.split(",")))

I1 = int(input("Enter the first index:\n"))
I2 = int(input("Enter the second index:\n"))

a=new_tuple(b,I1,I2)
print(a)