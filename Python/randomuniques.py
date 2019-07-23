import random
lst = []
for i in range(20):
    cond = True
    while cond:
        r = random.randint(1,20)
        if r not in lst:
            lst += [r]
            cond = False
print(lst)