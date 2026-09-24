def f(n):
    s = ''
    while n > 0:
        s = str(n % 2) + s
        n //= 2
    return s

def q(n):
    n_s = f(n)
    a = n_s.count('1')
    if a % 2 == 0:
        n_s = '10' + n_s[2:] + '0'
    else:
        n_s = '11' + n_s[2:] + '1'
    return int(n_s, 2)

for i in range(1, 1000):
    r = q(i)
    if r >= 16:
        print(i)
        break

