def f(a):
    b=""
    while a>0:
        b=str(a%2)+b
        a=a//2
    return b

t=8e10
for a in range(1,1000):
    b=f(a)
    if a%2==0:
        b='11'+b+'11'
    else:
        b='1'+b+'00'
    t=int(b,2)
    if t>95:
        print(t)
        break