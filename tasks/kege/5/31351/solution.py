t=float('inf')
for a in range(1,1000):
    b=bin(a)[2:]
    if b.count('1')%2==0:
        b='10'+b[2:]+'0'
    else:
        b='11'+b[2:]+'1'
    t=int(b,2)
    if t>16:
        print(a)
        break