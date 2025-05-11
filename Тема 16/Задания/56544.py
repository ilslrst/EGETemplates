
def f(a,b):

    if b == 0:
        return 0

    elif a > b:
        return f(a-1,b) + b

    elif b >= a  and b > 0:
        return f(a,b-1) + a

for a in range(1, 10):
    for b in range(10):

        print(a,b,f(a,b))

# /////////////////////////////////////////////////////////

count = 0
c = 2097152
for b in range(1, 2097153):
    if c % b == 0:
        count += 1
print(count)