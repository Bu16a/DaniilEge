def f(x, y, w, z):
    return (w == z) or not(y <= w) or not(x)
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not f(x, y, w, z):
                    print(x, y, w, z)

#ywxz