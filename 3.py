def palindrome(num):
    rev_num = 0
    num_copy = num
    while num > 0:
        r = num%10
        rev_num = (rev_num*10) + r
        num = num//10
    if num_copy == rev_num:
        print("It's Palindrome")
    else:
        print("It's not a palindrome")

a = int(input("Enter a number\n"))
palindrome(a)