a = input("Enter 1st string\n")
b = input("Enter 2nd string\n")
if len(a) == len(b):
    if sorted(a) == sorted(b):
        print("These strings are anagrams of each other.")
    else:
        print("These strings are not anagrams of each other.")
else:
    print("These strings are not anagrams of each other.")
