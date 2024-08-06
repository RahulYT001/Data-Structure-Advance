def length(l1, l2):
    if len(l1) > len(l2):
        return l1
    else:
        return l2
    
def union(l1, l2):
   
    k1 = list(set(l1))
    k2 = list(set(l2))
    

    longer_list = length(k1, k2)
    
   
    union = []
    
  
    if longer_list == k1:
        for i in k1:
            if i not in k2:
                union.append(i)
    else:
        for i in k2:
            if i not in k1:
                union.append(i)
    
    for i in (k1 if longer_list == k2 else k2):
        if i not in union:
            union.append(i) 
    return union


list1 = [1, 2, 2, 3, 4]
list2 = [2, 2, 4, 6]
union_result = union(list1, list2)
print(union_result) 
