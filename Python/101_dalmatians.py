def how_many_dalmatians(n):
    dogs = ["Hardly any", "More than a handful!", "Woah that's a lot of dogs!", "101 DALMATIONS!!!"]
    q = [10,50,100,101]
    c = 0
    while c < 4:
        if n <= q[c]:
            respond = dogs[c]
            c = 4
        else:
            c += 1
    return respond
print(how_many_dalmatians(102))