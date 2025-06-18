class Solution(object):
    def isMonotonic(self, nums):

       test = True

       if len(nums) == 1:
        return True

       for i in range(0,len(nums)-1) :
        if nums[i] == nums[i+1]:
         sens = 0
         if i == len(nums)-1:
          break
        elif nums[i] > nums[i+1]:
         sens = -1
         break
        else:
         sens = 1
         break

       if sens == 1 :
         for i in range(0,len(nums)-1):
          if nums[i+1] < nums[i]:
           return False

       elif sens == -1:
         for i in range(0,len(nums)-1):
          if nums[i+1] > nums[i]:
           return False
       
       return True
       


tab = [2,2,2,1,1,1]
solution = Solution()
result = solution.isMonotonic(tab)
print(result)
        