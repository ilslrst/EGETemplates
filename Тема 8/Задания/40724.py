import itertools
from itertools import repeat

x = itertools.permutations("СВЕТЛАНА", 8)
count = 0
words = set()

for str in x:
    line = "".join(str)

    if line.count("АА") == 0:

        words.add(line)
        count += 1

print(count//2)
print(len(words))