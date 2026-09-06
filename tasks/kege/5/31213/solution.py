def f(a):
    b=""
    while a>0:
        b=str(a%2)+b
        a=a//2
    return b

t=8e10
for a in range(17,1000):
    b=f(a)
    if a%2==0:
        b='10'+b
    else:
        b='1'+b+'01'
    t=min(t,int(b,2))
print(t)