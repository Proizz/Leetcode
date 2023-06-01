class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        fb_list = []
        for i in range(1, n+1):
            if i % 5 == 0 and i % 3 == 0:
                fb_list.append("FizzBuzz")
            elif i % 5 == 0:
                fb_list.append("Buzz")
            elif i % 3 == 0:
                fb_list.append("Fizz")
            else:
                fb_list.append(str(i))
        return fb_list


s = Solution()

n = 3
print(n)
print(s.fizzBuzz(n))
print()

n = 5
print(n)
print(s.fizzBuzz(n))
print()

n = 15
print(n)
print(s.fizzBuzz(n))
print()
