t = float('inf')
for a in range(1, 1000):
    b = bin(a)[2:]
    if a % 2 == 0:
        b = '11' + b + '11'
    else:
        b = '1' + b + '00'
    t = int(b, 2)
    if t > 95:
        print(t)
        break
