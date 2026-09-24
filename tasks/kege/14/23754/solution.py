a = 9 * 11 ** 210 + 8 * 11 ** 150
for x in range(1, 3001):
    n = a - x
    count = 0
    while n > 0:
        if n % 11 == 0:
            count += 1
        n //= 11
    if count == 60:
        print(x)
