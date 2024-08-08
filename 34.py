def dict_sort(d):
    d2 = {}
    sorted_values = sorted(d.values())
    
    for value in sorted_values:
        for key in d:
            if d[key] == value and key not in d2:
                d2[key] = value
                break
    return d2

my_dict = {
    'a': 3,
    'b': 1,
    'c': 2,
    'd': 5
}

a = dict_sort(my_dict)
print(a)
    

