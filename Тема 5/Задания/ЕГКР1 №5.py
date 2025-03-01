def to_ternary(n):
    if n == 0:
        return "0"
    ternary = ""
    while n > 0:
        ternary = str(n % 3) + ternary
        n //= 3
        return ternary
for g in range(100):
    b = to_ternary(g)

    if g % 3 == 0:
        p = g % 1000
        res = "g" + "p"
        print(res)

    else:
            g = b.count('1') + b.count('2') * 2
            b += to_ternary(g)
        r = int(b, 3)
    if r > 220 and r % 2 == 0:
        print(r)
        break


