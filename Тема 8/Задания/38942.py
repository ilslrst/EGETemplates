from itertools import product, repeat, count

s = product("АВОРТ", repeat = 4)
count = 1
for i in s:
    p = "".join(i)
    if p == "РОТА":
        print(count)
    count + 1