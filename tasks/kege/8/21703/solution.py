from itertools import product

a = product('АБДЕОП', repeat=6)
c = 0
count = 0
for i in a:
    s = ''.join(i)
    c += 1
    if s[0] != 'О':
        continue

    if s.count('П') != 1:
        continue

    if s.count('Б') != 1:
        continue

    if s.count('Е') != 1:
        continue

    if s.count('Д') != 1:
        continue

    if s.count('А') != 1:
        continue
    if c % 2 == 0:
        count = c

print(count)
