def count_vowels(str):
    v = "AEIOUaeiou"
    count = 0
    for k in str:    
        if k in v:
            count+=1
    print(count)

a=input("Enter the string\n")
count_vowels(a)