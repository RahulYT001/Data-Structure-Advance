import random

l = [1, 2, 34, 45, 5]
index = []
shuffled_index = []
shuffled_list = []
i = 0

while i < len(l):
    index.append(i)
    i += 1

while index:
    random_index = random.choice(index)
    shuffled_index.append(random_index)
    index.remove(random_index)

for ind in shuffled_index:
    shuffled_list.append(l[ind])

print(shuffled_list)
