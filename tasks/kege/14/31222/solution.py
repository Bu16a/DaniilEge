a = int('76079645', 19) + int('35042', 19) + int('33206', 19)
b = 0
for i in range(1, 19):
    c = a + i * (19 ** 5) + i * (19 ** 2) + i * 19
    if a % 18 == 0:
        b = max(b, c)
print(b / 18)
