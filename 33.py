a = input("Enter your keys with commas: \n")
list1 = list(j.strip() for j in a.split(","))

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

current = nested_dict
for key in list1:
    if key in current:
        current = current[key]
    else:
        print(None)
        break
else:
    print(current)
