my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}

inverted = {}
for key, value in my_dict.items():
    if value in inverted:
        inverted[value].append(key)
    else:
        inverted[value] = [key]

print(inverted)
