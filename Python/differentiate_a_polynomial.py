def differentiate(t, x):
    c,e,n = [],[],t.count('x')
    while t.count('x') > 0:
        i = t.index('x')
        jp = t.index('+',i) if '+' in t[i:] else len(t) - 1
        jm = t.index('-',i) if '-' in t[i:] else len(t) - 1
        j = min(jp,jm)
        c += [1] if i == 0 else [-1] if t[i-1] == '-' else [int(t[:i])]
        if (i < len(t) - 1) and (t[i+1] == '^'):
            e += [int(t[i+2:j])] if j < len(t) - 1 else [int(t[i+2:j+1])]
        else:
            e += [1]
        t = t[j+1:] if t[j] == '+' else t[j:] if  t[j] == '-' else ''
    return sum(c[i]*e[i]*x**(e[i]-1) for i in range(n))
print(differentiate('21x^4+3',414))