# import sys
# sys.setrecursionlimit(10**8)
#
# def f(n):
#     if n<20:
#         return n
#     if n>=20:
#         return (n-3)*f(n-5)
#
# print(f(44652) - 350 * f(44647)/f(44642))

f = [0]*50000

for i in range(1,50000):
    if i<20:
        f[]