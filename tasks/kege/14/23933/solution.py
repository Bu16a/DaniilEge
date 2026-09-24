for x in range(8, 37):
    a = int('11353712', x) + int('135421', x)
    if a % 31 == 0:
        print(a // 31)
