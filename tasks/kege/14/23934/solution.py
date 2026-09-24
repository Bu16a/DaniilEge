for x in range(7, 37):
    a = int('2465123', x) + int('251341', x)
    if a % 17 == 0:
        print(a // 17)