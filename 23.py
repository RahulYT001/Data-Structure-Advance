def join(t1,t2):
    t3= t1+t2
    print(t3)

a = input("Enter your numbers with commas for Tuple 1: \n")
t1 = tuple(map(int, a.split(",")))

b = input("Enter your numbers with commas for Tuple 2: \n")
t2 = tuple(map(int, b.split(",")))
join(t1,t2)