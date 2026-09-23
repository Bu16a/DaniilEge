from itertools import product

a = product('012345678', repeat=6)
p = 0
count = ''
for i in a:
    s = ''.join(i)
    if s[0] == '0':
        continue
    p += 1
    if p % 10 != 5:
        continue

    mask = ''
    for j in s:
        mask += str(int(j) % 2)

    if '11' in mask:
        continue
    count = s

print(count)
