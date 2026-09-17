def f(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s


def q(n):
    n_s = f(n)
    if n % 2 == 0:
        n_s = '10' + n_s
    else:
        n_s = '1' + n_s + '01'
    return int(n_s, 2)


mn = float('inf')
for n in range(17, 1000):
    r = q(n)
    if r < mn:
        mn = r
print(mn)
