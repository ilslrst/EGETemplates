for n in range(1, 100):
    b = bin(n)[2:]

    z = int(b)
    p = int(b)
    z = b.count("1")[::2]
    p = b.count("0")[1::2]

    r = z - p
    if r == 5:
        print(n)
        break


