def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s

def q(n):
    n_s = f(n)
    if n % 3 == 0:
        n_s = '1' + n_s + '21'
    else:
        a = f((n % 3) * 5)
        n_s = n_s + a
    return int(n_s, 3)

for i in range(1, 1000):
    r = q(i)
    if r <= 1130:
        print(i)