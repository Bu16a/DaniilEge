for x in range(16, 37):
    a = int('22A12E', x) + int('2F1391', x) - int('1H05D0', x)
    if a % 19 == 0:
        print(a // 19)