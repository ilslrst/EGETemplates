import itertools

op = "012345678"

count = 0

for line in itertools.product(op,op,op,op,op,op):
    line="".join(line)

    if line.count("1") >= 2 and (line[0] != "0" and line[0] != "1" and line[0] != "3" and line[0] != "5" and line[0] != "7") and (line[5] != "2" and line[5] != "3"):

        count += 1
print(count)