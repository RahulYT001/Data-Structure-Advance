def input_set(value):
    return set(value)

set1 = input_set(input("Enter the first set of characters (without spaces, e.g., abcdef):\n"))
set2 = input_set(input("Enter the second set of characters (without spaces, e.g., ghijk):\n"))

union_set = set1.union(set2)
print("Union of the two sets:", union_set)
