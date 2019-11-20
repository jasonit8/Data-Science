def knight(p1, p2):
    a = ['a','b','c','d','e','f','g','h']
    n = [1,2,3,4,5,6,7,8]
    r = [p1]
    c = 0
    while p2 not in r:
        c += 1
        r0 = []
        for p in r:
            za = a.index(p[0])
            zn = n.index(int(p[1]))
            for i in [-2,-1,1,2]:
                for j in [-2,-1,1,2]:
                    if i+j in [-3,-1,1,3]:
                        r0 += [a[za+i]+str(n[zn+j])] if (za+i in range(8)) and (zn+j in range(8)) else []
        r = r0
    return c
print(knight('f2','e7'))