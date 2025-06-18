class Solution(object):
    def findTheDifference(self, s, t):
     s = sorted(s)
     t = sorted(t)

     for i in range(len(s)):
      if s[i] != t[i]:
       return t[i]
     return t[-1]
     


solution = Solution()
result = solution.findTheDifference("abcd", "abced")
print(result)

        
        
        