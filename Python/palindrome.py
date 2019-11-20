def permute_a_palindrome(t):
    c = 0
    l = list(t)
    for i in set(l):
        c += 1 if l.count(i) % 2 == 1 else 0
    return c < 2
print(permute_a_palindrome('et'))