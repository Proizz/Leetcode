def moveZeroes(nums):
    if len(nums) > 0:
        for i in range(0, len(nums)):
            j = i + 1
            if j > len(nums) - 1 :
                break
            if nums[i] == 0:
                while nums[j] == 0 and j < len(nums) -1:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]




test = [0, 1 ]
moveZeroes(test)
print(test)


test = [1, 0 ]
moveZeroes(test)
print(test)

test = [0,1,0,3,12, 0]
moveZeroes(test)
print(test)