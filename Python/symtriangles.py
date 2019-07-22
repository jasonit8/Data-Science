# Draw 2 symmetric isosceles right triangles with respect to a vertex.
n = int(input('Length of one edge: '))
s = ['*']+['']*(n-2)+['* '*(2*n-1)]+['']*(n-2) + ['  '*(2*n-2)+'*']
l = len(s)
for i in range(1,n-1):
    s[i] = '* ' + '  '*(i-1) + '* '
    s[l-i-1] = '  '*(l-i-1) + '* ' + '  '*(i-1) + '* '
for i in s:
    print(i)
