class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth = [sum(acc) for acc in accounts]
        return max(wealth)


s = Solution()
accounts = [[1, 2, 3], [3, 2, 1]]
output = s.maximumWealth(accounts)
print(accounts)
print(output)
print()

accounts = [[1, 5], [7, 3], [3, 5]]
output = s.maximumWealth(accounts)
print(accounts)
print(output)
print()

accounts = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
output = s.maximumWealth(accounts)
print(accounts)
print(output)
print()
