def merge(l1,l2):
    i,j = 0,0
    l3=[]
    while i<len(l1) and j < len(l2):
        if l1[i]<l2[j]:
            l3.append(i)
            i+=1
        else:
            l3.append(j)
            j+=1

    while i < len(l1):
        l3.append(l1[i])
        i += 1
    
    
    while j < len(l2):
        l3.append(l2[j])
        j += 1

    print(l3)

l1=[1,34,56]
l2=[2,3,4,5,6]
merge(l1,l2)

