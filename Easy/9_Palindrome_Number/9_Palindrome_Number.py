class Solution:
    def isPalindrome( x: int) -> bool:
        li_num = []
        if x < 0:
            return False
        n = 0
        while x - 10 ** n >= 0:
            n += 1
        n -= 1
        while n >= 0:
            li_num.append(x // 10 ** n)
            x %= 10 ** n
            n -= 1
        rev_li_num = li_num.copy()
        rev_li_num.reverse()
        for i in range(len(li_num)):
            if li_num[i] != rev_li_num[i]:
                return False
        return True


x = 121
print(Solution.isPalindrome(x))

x = -121
print(Solution.isPalindrome(x))

x = 10
print(Solution.isPalindrome(x))

x = 12322399322321
print(Solution.isPalindrome(x))

x = 8888228888
print(Solution.isPalindrome(x))

x = 88882128888
print(Solution.isPalindrome(x))

x = 888821228888
print(Solution.isPalindrome(x))



