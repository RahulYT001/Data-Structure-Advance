def value(d,l):
    current = d
    for key in l:
        if key in current:
            current = current[key]
        else:
            return None
    return current

    


a = input("Enter your keys with commas: \n")
list1 = list(j.strip() for j in a.split(","))


#Adding an example list as well for better understanding.
# keys_list = ['a', 'b', 'c']

nested_dict = {
    'a': {
        'b': {
            'c': 42
        }
    },
    'x': {
        'y': {
            'z': 99
        }
    }
}

print(value(nested_dict,list1))