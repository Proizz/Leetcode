"""   def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Solution works, but i will try it without two dicts.
        dict_mag = {}
        dict_ran = {}
        for chr in magazine:
                dict_mag[chr] = 0
        for chr in magazine:
                dict_mag[chr] += 1
        for chr in ransomNote:
                dict_ran[chr] = 0
        for chr in ransomNote:
                dict_ran[chr] += 1
        for key in dict_ran:
            if key in dict_mag:
                if dict_ran[key] <= dict_mag[key]:
                    continue
                else:
                    return False
            else:
                return False
        return True"""

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict_mag = {}
        for chr in magazine:
                dict_mag[chr] = 0
        for chr in magazine:
                dict_mag[chr] += 1
        for chr in ransomNote:
            if chr in dict_mag:
                if dict_mag[chr] > 0:
                    dict_mag[chr] -= 1
                    continue
                else:
                    return False
            else:
                return False
        return True

ransomNote = "bfhb"
magazine = "bfhakbbb"
s = Solution()
print(ransomNote, magazine)
print(s.canConstruct(ransomNote, magazine))
print()
