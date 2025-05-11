import sys
sys.setrecursionlimit(10**6)


def f(n):
    if n < 15:
        return n
    elif n >= 15:
        return f(n // 15) * f(n % 15)
    count = 0
    if f(n) == 7560 and n < 3**40:
        count+=1

        print(count)


