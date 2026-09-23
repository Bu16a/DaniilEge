from itertools import product

a = product('0123456789ABC', repeat=3)
p = 0
count = 0
for i in a:
    p += 1
    s = ''.join(i)
    if s[0] == '0' or p % 10 != 7:
        continue

    mask = ''
    for j in s:
        mask += str(int(j, 13) % 2)

    if '11' in mask:
        continue
    count += 1

print(count)
