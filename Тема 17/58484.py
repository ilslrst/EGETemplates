nums = list(map(int, open("17.txt").readlines()))

count1 = 0
count = 0
for min_ in range(99, 1000):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (len(str(nums[i])) == 4 != (len(str(nums[i+1])) == 4):






