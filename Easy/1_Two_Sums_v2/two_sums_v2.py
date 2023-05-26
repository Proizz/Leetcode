import random


class Solution:

    def twoSum(nums: list[int], target: int) -> list[int]:
        map_dict = {}
        for i in range(len(nums)):
            y = target - nums[i]
            if y in map_dict:
                return [map_dict.get(y), i]
            map_dict.update({nums[i]: i})
        return [0, 0]


nums = [2, 7, 11, 15]
target = 9
print(Solution.twoSum(nums=nums, target=target))

nums = [3, 2, 4]
target = 6
print(Solution.twoSum(nums=nums, target=target))

nums = [3, 3]
target = 6
print(Solution.twoSum(nums=nums, target=target))

nums = [random.randint(0,20) for i in range(10)]
target = 15
print(nums)
print(target)
print(Solution.twoSum(nums=nums, target=target))