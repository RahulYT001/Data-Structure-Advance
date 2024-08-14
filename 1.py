rev_str = ""
length = len(a := input("Enter the string to be reversed: "))
while length > 0:
    rev_str += a[length - 1]
    length -= 1
print(rev_str)
