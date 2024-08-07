def merge_dictionaries(dict1, dict2):
    merge = {}
    d1_items = dict1.items()
    d2_items = dict2.items()

   
    for i in d1_items:
        merge[i[0]] = i[1]
    for j in d2_items:
        if j[0] in merge:
            merge[j[0]]+=j[1]
        else:
            merge[j[0]] = j[1]
    return merge

dict1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dict2 = {
    'b': 3,
    'c': 4,
    'd': 5
}

merged_dict = merge_dictionaries(dict1, dict2)
print("Merged dictionary:", merged_dict)