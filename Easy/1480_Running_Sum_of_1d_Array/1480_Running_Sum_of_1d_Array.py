"""def runningSum2(self, nums: list[int]) -> list[int]:
        run_nums = nums.copy()
        for i in range(len(run_nums)):
            for j in range(i):
                run_nums[i] += nums[j]
        return run_nums

def runningSum3(self, nums: list[int]) -> list[int]:
        run_nums = nums.copy()
        for i in range(1, len(run_nums)):
            run_nums[i] += run_nums[i - 1]
        return run_nums"""


class Solution:

    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


s = Solution()
nums = [1, 2, 3, 4]
run_nums = s.runningSum(nums)
print(nums)
print(run_nums)
print()

nums = [1, 1, 1, 1, 1]
run_nums = s.runningSum(nums)
print(nums)
print(run_nums)
print()

nums = [3, 1, 2, 10, 1]
run_nums = s.runningSum(nums)
print(nums)
print(run_nums)
print()
