def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n = n // 7
    return s

def q(n):
    n_s = f(n)
    if n % 7 == 2:
        n_s = n_s.replace('3', '#')
        n_s = n_s.replace('1', '3')
        n_s = n_s.replace('#', '1')
        n_s = '21' + n_s
    else:
        n_s = '1' + n_s[1:] + '36'
    return int(n_s, 7)
x = 0
m = 0
for i in range(1, 1000):
    r = q(i)
    if r < 744:
        if r > m:
            m = r
            x = i
print(x)