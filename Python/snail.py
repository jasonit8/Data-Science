# def snail(m):
#     if len(m) <= 1:
#         a = m[0]
#     else:
#         r,c,d = 0,0,0
#         a = [m[r][c]]
#         m[r][c] = 'x'
#         stop = 2
#         while stop > 0:
#             if d > 3:
#                 d -= 4
#             if d == 0:
#                 if m[r][c+1] == 'x':
#                     stop -= 1
#                     d += 1
#                 else:
#                     while (c+1 < len(m[r])) and m[r][c+1] != 'x':
#                         c += 1
#                         a += [m[r][c]]
#                         m[r][c] = 'x'
#                     else:
#                         d += 1
#             elif d == 1:
#                 if m[r+1][c] == 'x':
#                     stop -= 1
#                     d += 1
#                 else:
#                     while (r+1 < len(m)) and m[r+1][c] != 'x':
#                         r += 1
#                         a += [m[r][c]]
#                         m[r][c] = 'x'
#                     else:
#                         d += 1
#             elif d == 2:
#                 if m[r][c-1] == 'x':
#                     stop -= 1
#                     d += 1
#                 else:
#                     while (c-1 >= 0) and m[r][c-1] != 'x':
#                         c -= 1
#                         a += [m[r][c]]
#                         m[r][c] = 'x'
#                     else:
#                         d += 1
#             elif d == 3:
#                 if m[r-1][c] == 'x':
#                     stop -= 1
#                     d += 1
#                 else:
#                     while (r-1 >= 0) and m[r-1][c] != 'x':
#                         r -= 1
#                         a += [m[r][c]]
#                         m[r][c] = 'x'
#                     else:
#                         d += 1
#             else:
#                 pass
#     return a
def snail(m):
    a = []
    while m != []:
        a += m[0]
        del(m[0])
        m = list(zip(*m))[::-1]
    return a

m = [[1,2,3,4,5],
     [12,13,14,15,6],
     [11,10,9,8,7]]
print(snail(m))