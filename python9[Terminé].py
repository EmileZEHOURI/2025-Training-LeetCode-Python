class Solution(object):

    def moveZeroes(self, nums):
      insert_pos = 0

      for i in range(len(nums)):
       if nums[i] != 0:
        nums[insert_pos] = nums[i]
        if insert_pos != i:
         nums[i] = 0
        insert_pos += 1
      

      print(nums)


nums = [0,1,0,3,12]
solution = Solution()
result = solution.moveZeroes(nums)

print(result)