import random
lst = [random.randint(1,20) for i in range(20)]
for i in range(len(lst)):
    while lst.count(lst[i]) > 1:
        lst[i] = random.randint(1,20)
print(lst)
