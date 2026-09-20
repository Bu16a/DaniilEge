def f2(n, sys):
    c = 0
    for i in n:
        if i.isdigit():
            v = int(i)
        else:
            v = ord(i) - ord('A') + 10
        c = c * sys + v
    return c



for i in range(33, 100):
    if f2('KOT', i) + f2('GOLODNI', i) == f2('MEEOW', i)*f2('100', i) - f2('20194023088', 10):
        print(f2('PURR', i),i)
        break
