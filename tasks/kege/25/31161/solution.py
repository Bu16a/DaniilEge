def f(a):
    b = []
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            b.append(i)
            b.append(a//i)
    return b


s = 0
for i in range(8117600757, 10000000000):
    b = f(i)
    d=[]
    for j in b:
        if len(f(j))==0:
            d.append(j)
    if len(d)==0:
        continue
    M = int(d[-1]) - int(d[0])
    m = f(M)
    if len(m) == 0 and str(M).count('1') >= 4:
        print(i, M)
        s += 1
    if s == 5:
        break