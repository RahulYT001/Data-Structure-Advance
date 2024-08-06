def check_asc(l):
    i=1
    while i < (len(l)):
        if l[i]>l[i-1]:
            i+=1
        else:
            return False
    return True
           
def check_desc(l):
    i=1
    while i < (len(l)):
        if l[i]<l[i-1]:
            i+=1
        else:
            return False
    return True

l = [1,2,4,5]
a= check_asc(l)
b=check_desc(l)

if not a and not b:
    print("It is not sorted.")
elif a:
    print("It is in ascending order.")
elif b:
    print("It is in descending order.")