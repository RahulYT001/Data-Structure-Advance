l = [1, 2343, 5345, 532, 121]
num = list(set(l))
largest = float('-inf')
second_largest = float('-inf')

for num in num:
    if num > largest:
        second_largest = largest
        largest = num
    elif (num > second_largest) and (num != largest):
        second_largest = num

print(second_largest)
