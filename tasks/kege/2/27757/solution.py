for x in range(0, 2):
    for y in range(0, 2):
        for w in range(0, 2):
            for z in range(0, 2):
                if (not (x) and y and z and not (w)) or (not (x) and y and not (z) and not (w)) or (
                        x and y and z and not (w)):
                    print(x, w, z, y)
