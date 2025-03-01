import itertools
from itertools import product, repeat

count = 1

for x in product("АМУХ", repeat=4):
    if "".join(x) == "ХУХХ":
        break
    count += 1

print(count)
