def invert_dict(d):
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            inverted[value].append(key)
        else:
            inverted[value] = [key]
    return inverted



my_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2
}


inverted_dict = invert_dict(my_dict)
print(inverted_dict)  