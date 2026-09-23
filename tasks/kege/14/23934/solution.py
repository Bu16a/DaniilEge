for i in range(7, 37):
    d = int('2465123', i) + int('251341', i)
    if d % 17 == 0:
        print(d // 17)
        break