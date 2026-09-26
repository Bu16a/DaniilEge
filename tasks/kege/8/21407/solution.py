from itertools import product

a = product('ДГИАШЭ', repeat=5)
p='ИАЭ'
count = 0
for i in a:
    s = ''.join(i)

    mask = ''
    for j in s:
        if j in p:
            mask = mask + '1'
        else:
            mask = mask + '0'

    if mask[0] == '1' or mask[4] == '0':
        continue
    count += 1

print(count)