class Solution:

    def romanToInt(s: str) -> int:
        ro_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_int = 0
        for i, char in enumerate(s):
            if i < len(s)-1:
                if char == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    sum_int -= ro_dict.get(char)
                    continue
                if char == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    sum_int -= ro_dict.get(char)
                    continue
                if char == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    sum_int -= ro_dict.get(char)
                    continue
            sum_int += ro_dict.get(char)
        return sum_int


s = "III"
print(Solution.romanToInt(s))

s = "LVIII"
print(Solution.romanToInt(s))

s = "MCMXCIV"
print(Solution.romanToInt(s))
