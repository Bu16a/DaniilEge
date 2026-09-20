a = 7 ** 270 + 7 ** 170 + 7 ** 70
k = '0123456'


def f(a):
    b = ''
    while a > 0:
        b = str(k[a % 7]) + b
        a = a // 7
    return b


o = 0
p = 0
for i in range(1,11500):
    d = a - i
    g = f(d)
    if g.count('0') >= p:
        p = g.count('0')
        o = i
print(o)
