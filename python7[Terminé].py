class Solution(object):
    def isAnagram(self, s, t):
        s = sorted(s)
        t = sorted(t)

        if s == t:
         return True
        else:
         return False
      
solution = Solution()
result = solution.isAnagram("anagram", "nagaram")

print(result)