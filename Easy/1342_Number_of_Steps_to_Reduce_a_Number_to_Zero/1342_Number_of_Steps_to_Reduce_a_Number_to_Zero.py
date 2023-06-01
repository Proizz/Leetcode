class Solution:
    def numberOfSteps(self, num: int) -> int:
        counter = 0
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            counter += 1
        return counter

    def numberOfStepsBitwise(self, num):
        counter = 0
        while num > 0:
            if num & 1:
                num >>= 1
            else:
                num -= 1
            counter += 1
        return counter

s = Solution()
num = 14
print(num)
print(s.numberOfSteps(num))
print(s.numberOfStepsBitwise(num))
print()

num = 8
print(num)
print(s.numberOfSteps(num))
print()

num = 123
print(num)
print(s.numberOfSteps(num))
print()
