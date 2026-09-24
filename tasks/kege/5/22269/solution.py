def f(n):
    s = ''
    while n > 0:
        s = str(n % 5) + s
        n = n // 5
    return s

def q(n):
    n_s = f(n)
    if n % 5 == 0:
        n_s = n_s.replace('1', '#')
        n_s = n_s.replace('4', '1')
        n_s = n_s.replace('#', '4')
        n_s = '33' + n_s
    else:
        n_s = '3' + n_s[1:] + '42'
    return int(n_s, 5)

m = 0
for i in range(1, 1000):
    r = q(i)
    if m < r < 1922:
        m = r
        print(i)