l = [1, 2, 4, 5]

i = 1
while i < len(l):
    if l[i] > l[i-1]:
        i += 1
    else:
        a = False
        break
else:
    a = True

i = 1
while i < len(l):
    if l[i] < l[i-1]:
        i += 1
    else:
        b = False
        break
else:
    b = True

if not a and not b:
    print("It is not sorted.")
elif a:
    print("It is in ascending order.")
elif b:
    print("It is in descending order.")
