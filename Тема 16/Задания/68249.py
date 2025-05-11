def f(n):
    if n == 0:
        return 0
    elif n%2 != 0:
        return f(n-1) + 2*n - 1

    elif n%2 == 0:
        return 4*f(n/2)

for a in range(10):
    for n in range(10):

        print(a,f(a), n,f(n))

# ///////////////////////////////////////////////////

for a in range(10000):
    for n in range(10000):
        if a**2 - n**2 == 1001:
            print(a-n)










