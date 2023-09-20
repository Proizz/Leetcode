def remove_elements_two(nums , val):
    leng=0
    if len(nums) > 0:
        for i in range(0, len(nums)):
            j = i + 1
            if j > len(nums) - 1 :
                break

            if nums[i] == val:
                while nums[j] == val and j < len(nums) -1:
                    j += 1
                nums[i], nums[j] = nums[j], nums[i]
        for i in nums:
            if i == val:
                break
            leng+=1
    return leng



test = [0,1,2,2,1,1,1 ,1 ]
value = 1
k= remove_elements_two(test,value)
print(test , k)