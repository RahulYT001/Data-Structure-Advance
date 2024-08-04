def case_change(a,b):
    if b==1:
        print(a.upper()) 
    elif b==2:
        print(a.lower())
    else:
        print("Enter a valid input")
while True:
    print("      Menu")
    print("1. Upper_case\n2. Lower_case\n3. Exit")
    b=int(input("Press 1, 2 or 3\n"))
    if b == 3:
        print("Exited..")
        break
    else:
        a=input("Enter the string\n")
        r = case_change(a,b)
  