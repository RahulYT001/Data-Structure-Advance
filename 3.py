a = int(input("Enter a number\n"))
rev_num = 0
num_copy = a
while a > 0:
    r = a % 10
    rev_num = (rev_num * 10) + r
    a = a // 10
if num_copy == rev_num:
    print("It's Palindrome")
else:
    print("It's not a palindrome")
