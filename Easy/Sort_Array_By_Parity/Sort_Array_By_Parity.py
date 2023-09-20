def sortArrayByParity(nums):
    if len(nums) > 0:
        for i in range(0, len(nums)):
            j = i + 1
            if j > len(nums) - 1 :
                break

            if nums[i]%2 == 1:
                while nums[j]%2 == 1 and j < len(nums) -1:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]




test = [0, 1 ]
sortArrayByParity(test)
print(test)


test = [1, 0 ]
sortArrayByParity(test)
print(test)

test = [3,1,2,4]
sortArrayByParity(test)
print(test)