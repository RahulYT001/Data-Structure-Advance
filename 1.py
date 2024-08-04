def rev(str):
    rev_str = ""
    length = len(str)
    while length>0:
        rev_str+=str[length-1]
        length-=1
    return rev_str

a=input("Enter the string to be reversed")
print(rev(a))