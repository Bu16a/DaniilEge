def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s

def q(n):
    n_s = f(n)
    if n % 3 == 0:
        n_s = n_s + n_s[-2:]
    else:
        b = n_s.count('1')
        c = n_s.count('2')
        d = f((b + c * 2) * 2)
        n_s = n_s + d
    return int(n_s, 3)
mn = float('inf')
for n in range(1, 1000):
    r = q(n)
    if r % 2 != 0 and r > 520 and r < mn:
        mn = r
print(mn)
