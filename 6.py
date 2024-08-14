count = 1
str_return = ""
a = input("Enter the string\n")
length = len(a)

for i in range(1, length):
    if (a[i] == a[i-1]):
        count += 1
    else:
        str_return += a[i-1] + f"{count}"
        count = 1

str_return += a[-1] + f"{count}"
print(str_return)
