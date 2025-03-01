import itertools

op = "012345678"

count = 0

for line in itertools.product(op,op,op,op,op,op):
    line = "".join(line)

    if line.count("1") + line.count("3") + line.count("5") + line.count("7") == 2 and line.count("4") == 1 and line[0] != "0":


        count += 1

print(count)