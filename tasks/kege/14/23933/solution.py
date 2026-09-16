for i in range(8, 37):
    d = int('11353712', i) + int('135421', i)
    if d % 31 == 0:
        print(d // 31)
        break
