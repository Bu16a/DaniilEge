def f(a):
    b = []
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            b.append(i)
            b.append(a//i)
    return b


s = 0
for i in range(1104285717, 10000000000):
    b = f(i)
    d=[]
    if len(b)!=2:
        continue
    for j in b:
        if len(f(j))==0:
            d.append(j)
    if len(d)<2:
        continue
    if len(b) == len(d) and str(d[0]).count('16') and str(d[1]).count('16'):
        print(i, min(d))
        s += 1
    if s == 5:
        break