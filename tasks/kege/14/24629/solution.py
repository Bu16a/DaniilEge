def f(a, sys):
    b = ''
    while a > 0:
        if a % sys <= 9:
            b = str(a % sys) + b
        else:
            b = chr(ord('A') + a % sys - 10) + b
        a = a // sys
    return b

a=14**1402+28**501-14*51-1400
b=f(a,14)
print(b.count('C'))