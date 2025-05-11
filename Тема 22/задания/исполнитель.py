def f(x, hod, res):
    if hod == 4:
        res.add(x)
        return
    f(x+2, hod+1, res)
    f(x*3, hod+1, res)

nums = set()
f(1, 0, nums)
print(len(nums))
