def find_nb(m):
    v,n = 0,0
    while v < m:
        v += (n + 1)**3
        n += 1
    else:
        return n - 1 if v == m else -1
print(find_nb(1071225))