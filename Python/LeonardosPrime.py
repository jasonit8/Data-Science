def nextprime(x):
    a = 1
    c = True
    while c:
        if x + a > 1 and all((x+a)%i != 0 for i in range(2,int((x+a)**.5+1))):
            c = False
        else:
            a += 1
    return x + a

q = int(input('Number of queries: '))
qs = []
for i in range(q):
    qs += [int(input('n%i: ' %(i + 1)))]
for i in qs:
    p, f = 1, 1
    c = 0
    while p*nextprime(f) <= i:
        f = nextprime(f)
        p *= f
        c += 1
    print(c)
