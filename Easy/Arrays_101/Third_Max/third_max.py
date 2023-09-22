def thirdMax(nums,):
    maxes = [max(nums)]
    for j in range(2):
        cur_i = min(nums)
        for i in nums:
            if i > cur_i and i < maxes[-1]:
                cur_i = i
        if maxes[-1] != cur_i:
            maxes.append(cur_i)
    if len(maxes) < 3:
        return maxes[0]
    else:
        return maxes[-1]


test = [3,2,1]
print(thirdMax(test))

test = [1, 2]
print(thirdMax(test))

test = [2,2,3,1]
print(thirdMax(test))
