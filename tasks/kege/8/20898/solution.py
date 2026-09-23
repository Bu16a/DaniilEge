from itertools import product

a = product('012345678', repeat=5)

count = 0
for i in a:
    s = ''.join(i)

    if s[0] == '0':
        continue

    if s.count('0') != 1:
        continue

    mask = ''
    for j in s:
        if int(j) == 0:
            mask = mask + 'P'
        else:
            mask = mask + str(int(j) % 2)

    if '1P' in mask or 'P1' in mask:
        continue
    count += 1

print(count)
