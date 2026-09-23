
def f2(n, sys):
    c = 0
    for i in n:
        if i.isdigit():
            v = int(i)
        else:
            v = ord(i) - ord('A') + 10
        c = c * sys + v
    return c

for x in range(10):
    a=int('10'+str(x))
    b=50-x
    c=int(str(x)+'13')
    if f2('SLADOST',36)+f2('GADOST',a)==f2('HALLOWEEN',b)-166729861760449:
        print(f2('GADOST',c))
        break