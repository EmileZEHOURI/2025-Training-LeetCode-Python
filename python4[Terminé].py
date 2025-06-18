class Solution(object):
    def mergeAlternately(self, word1, word2):

     a1 = list(word1)
     a2 = list(word2)


     maxlength = len(a1) + len(a2)

     c = []

     for i in range(maxlength):
      if i < len(a1):
       c.append(a1[i])
      if i < len(a2):
       c.append(a2[i])
      
    
     return ' '.join(c)   
    

word1 = "abc"
word2 = "pqr"
solution = Solution()
result = solution.mergeAlternately(word1, word2)

print(result)