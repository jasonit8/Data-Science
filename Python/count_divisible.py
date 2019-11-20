# def divisible_count(x,y,k):
#     return len([i for i in range(x,y+1) if i % k == 0])
def divisible_count(x,y,k):
    i,c = 1,0
    while i * k <= y:
        c += 1 if i * k in range(x,y+1) else 0
        i += 1
    return c

print(divisible_count(6,11000000,23))
