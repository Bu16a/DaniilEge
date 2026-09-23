for i in range(18, 37):
    d = int('22A12E', i) + int('2F1391', i) - int('1H05D0 ', i)
    if d % 19 == 0:
        print(d // 19)
        break