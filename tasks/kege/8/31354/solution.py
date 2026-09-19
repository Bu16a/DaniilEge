from itertools import product

t=0
m=0
a = product('ЕЛНОСЦ', repeat=6)
for i in a:
    t+=1
    if t%2==0:
        continue
    s = ''.join(i)

    if s[0] == 'Ц' or s[0] == 'Н':
        continue

    if s.count('Ц') != 1 or s.count('Н') != 1:
        continue

    m=t

print(m)