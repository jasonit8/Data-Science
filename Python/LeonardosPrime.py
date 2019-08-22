q = int(input('Number of queries: '))
qs = []
for i in range(q):
    qs += [[i for i in range(1,1+int(input('n%i: ' %(i+1))))]]
u = [0] * q
for i in range(q):
    for j in qs[i]:
        f = set()
        while j > 1:
            for k in range(2,int(j)+1):
                if j % k == 0:
                    f.add(k)
                    j /= k
                    break
        u[i] = len(f) if u[i] < len(f) else u[i]
for i in u:
    print(i)