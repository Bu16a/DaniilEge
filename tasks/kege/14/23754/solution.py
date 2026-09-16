a = 9 * 11 ** 210 + 8 * 11 ** 150
k = '0123456789ABCDEFG'


def f(a):
    b = ''
    while a > 0:
        b = b + str(k[a % 11])
        a = a // 11
    return b


p = 0
for i in range(3000):
    d = a - i
    g = f(d)
    if g.count('0') == 60:
        p = max(i, p)
print(p)
