p = range(25, 50)
q = range(32, 47)
maxl = 0
for v in range(70):
    for w in range(v, 70):
        a = range(v, w)
        if all(((x not in a) <= (x in p)) <= ((x in a) <= (x in q)) for x in range(70)):
            maxl = max(maxl, w - v)

print(maxl)






