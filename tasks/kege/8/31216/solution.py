from itertools import product
count = 0
nom=0
a = product('ВЕКОТЦ', repeat=6)
for i in a:
    s = ''.join(i)
    nom +=1
    if s.count('О')!= 3:
        continue
    if s.count('Т')!= 2:
        continue
    if s.count('Ц')!= 1:
        continue
    if nom%2==0:
        continue
    count += 1
print(count)

