def remove(l,a):
    index = []
    c=0
    for i in l:
        if i == a:
            index.append(c)
        c+=1
    index.sort()
    index.reverse()
    
    for k in index:
        l.pop(k)

    print(l)


l=[1,23,4,5,1,5,4]
print(f"The given list is {l}")
a = int(input("Enter the element that should be removed\n"))
remove(l,a)