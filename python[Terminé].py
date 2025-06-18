class Solution(object):
   def twoSum(self, nums, target):

      for i in range(len(nums)):
       for j in range(i + 1, len(nums)) :
        if nums[i] == nums[j]:
         print("i = j")
         pass
        if nums[i] + nums[j] == target:
         return [i, j]
        else :
         print("pas trouvé...")
         continue
      print("error : Pas de Solution")
      return 0



nums1 = [2,7,11,15] 
target1 = 9

solution1 = Solution()
result1 = solution1.twoSum(nums1,target1)
print("1: ", result1)

nums2 = [3,2,4]
target2 = 6

solution2 = Solution()
result2 = solution2.twoSum(nums2,target2)
print("2: ", result2)

nums3 = [3,3]
target3 = 6

solution3 = Solution()
result3 = solution3.twoSum(nums3,target3)
print("3: ", result3)

        