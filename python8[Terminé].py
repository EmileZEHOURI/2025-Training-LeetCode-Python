class Solution(object):
    def repeatedSubstringPattern(self, s):
        res = (s+s).find(s,1) != len(s)
        return res
      


solution = Solution()
result = solution.repeatedSubstringPattern("abcabcabcabc")

print(result)