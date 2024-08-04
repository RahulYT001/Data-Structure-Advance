def count_words(a):
    c=0
    words= a.split()
    for i in words:
        c+=1
    print(c)
a=input("Enter the string\n")
count_words(a)
