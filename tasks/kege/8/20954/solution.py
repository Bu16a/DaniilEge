from itertools import product

a = product('АКМС', repeat=6)
c=0
count = 0
for i in a:
    s = ''.join(i)
    c+=1

    if s.count('С') != 0 or s.count('М') != 0:
        continue
    if  s.count('КК') != 0:
        continue
    count = c

print(count)