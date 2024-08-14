my_dict = {
    'a': 3,
    'b': 1,
    'c': 2,
    'd': 5
}

d2 = {}
sorted_values = sorted(my_dict.values())

for value in sorted_values:
    for key in my_dict:
        if my_dict[key] == value and key not in d2:
            d2[key] = value
            break

print(d2)
