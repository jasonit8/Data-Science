def exp_sum(n):
    p = 0 # The partition.
    s = 1 # Keeps the loop.
    s0 = [[i] for i in range(n)] # Where we build up the sums.
    while s == 1: # While loop stops when 1+1+...+1=n occurs.
        for i in s0:
            for j in range(1,n-sum(i)+1):
                e = [] # new element
                e += i if i != [0] else []
                e += [j]
                e.sort()
                if (sum(e) <= n) and (e not in s0):
                    s0 += [e]
                    if sum(e) == n:
                        print(e)
                        p += 1
                        s -= 1 if e == [1]*n else 0
    return p
print(exp_sum(14))