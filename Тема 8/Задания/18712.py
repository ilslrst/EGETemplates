import  itertools
from itertools import repeat

x = itertools.product('ПРАВО', repeat=5)

count = 0

for str in x:
    line=''.join(str)

    if line.count('П') == 1:
        count += 1

print(count)