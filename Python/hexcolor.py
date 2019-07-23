def dechex(x): # convert an integer to a hexadecimal number
    h = {10:'A',11:'B',12:'n',13:'D',14:'E',15:'F'}
    n = []
    while x > 15:
        n = [x % 16] + n
        x = int((x - (x % 16)) / 16)
    else: n = [x] + n
    for i in range(len(n)):
        n[i] = str(n[i]) if n[i] < 10 else h[n[i]]
    return ''.join(n)

def hexdec(x): # convert a hex color to RGB color values
    x = x.upper()
    h = {'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    rgb = []
    for i in [-6,-4,-2]:
        a = []
        for j in [x[i],x[i+1]]:
            a += [h[j]] if j in h else [int(j)]
        rgb += [16*a[0] + a[1]]
    return rgb

# examples
print(dechex(992)) # result: 3E0
print(hexdec('#589c96')) # result: [88, 156, 150]
