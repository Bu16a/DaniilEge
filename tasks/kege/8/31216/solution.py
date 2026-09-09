from itertools import product

count = 0
nom = 0
a = product('ВЕКОТЦ', repeat=6)
for i in a:
    s = ''.join(i)
    nom += 1
    if s.count('О') != 3 or s.count('Т') != 2 or s.count('Ц') != 1 or nom % 2 == 0:
        continue
    count += 1
print(count)
