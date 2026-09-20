from itertools import product

count =
t=0
a = product('ВЕКОТЦ', repeat=6)
for i in a:
    t+=1
    if t%2==0:
        continue
    s = ''.join(i)

    if s.count('Т') != 2:
        continue

    if s.count('Ц') != 1:
        continue

    if s.count('О') != 3:
        continue

    count += 1

print(count)