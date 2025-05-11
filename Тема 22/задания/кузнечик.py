def f(x, hod, res):
    if hod == 68:
        return
    f(x + 3, hod + 1, res)
    f(x - 2, hod + 1, res)

nums = set()
f(1, 0 , nums)
print(len(nums))