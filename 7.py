def unique(a):
    b=set(a)
    if len(a) == len(b):
        print("It has all the unique characters.")
    else:
        print("This string doesn't have all unique characters.")                
    

a=input("Enter the string\n")
unique(a)