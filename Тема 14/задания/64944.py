for p in range(1,10):
    for x in range(1,p):
        for y in range(1,p):
            for z in range(1,p):
                for w in range(1,p):
                    res1 = (z * p ** 4) + (x * p ** 3) + (y * p ** 2) + (x * p ** 1) + (7 * p ** 0)
                    res2 = (x * p ** 4) + (y * p ** 3) + (8 * p ** 2) + (3 * p ** 1) + (6 * p ** 0)
                    res3 = (w * p ** 4) + (z * p ** 3) + (x * p ** 2) + (6 * p ** 1) + (4 * p ** 0)

                    if res1 + res2 == res3:
                        print((x*p**3)+(y*p**2)+(z*p**1)+(w*p**0))

