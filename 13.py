l = [1,23,45,6,54,3,1]
l.sort()
d={}

count = 1

for index in range(1,len(l)):
    if l[index] == l[index-1]:
        count+=1
    else:
        d[l[index-1]] = count
        count = 1
 
d[l[-1]] = count   
    


print(d.items())

