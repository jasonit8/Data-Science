def pyramid(b):
    n = int((1+(1+8*b)**.5)/2)
    return n if (n**2 + n)/2 <= b else n-1
print(pyramid(20))