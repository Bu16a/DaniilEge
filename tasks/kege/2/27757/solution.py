def f(x, y, w, z):
    return (not(x) and y and z and not(w)) or (not(x) and y and not(z) and not(w)) or (x and y and z and not(w))
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if f(x, y, w, z):
                    print(x, y, w, z)