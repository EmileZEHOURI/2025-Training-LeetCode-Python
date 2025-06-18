
class Solution(object):
 
    def arraySign(self, nums):

     product = nums
     s=1
     for i,a in enumerate(product):
      s*=a

     if s == 0:
         return 0
     elif s > 0:
         return 1
     else:
         return -1

tab = [-4,-2,5,3,-2,-4]

solution = Solution()
result = solution.arraySign(tab)
print(result)
        