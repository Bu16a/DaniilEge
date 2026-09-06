def f(a):
    b=""
    while a>0:
        b=str(a%2)+b
        a=a//2
    return b

t=8e10
for a in range(1,1000):
    b=f(a)
    if b.count('1')%2==0:
        b='10'+b[2:]+'0'
    else:
        b='11'+b[2:]+'1'
    t=int(b,2)
    if t>16:
        print(a)
        break