class Solution(object):
    def plusOne(self, digits):

     previous_dist = len(digits)
  
     
     for i in reversed(digits):
     
      digits[previous_dist-1] = i+1 
 
      if digits[previous_dist-1] != 10:
       return digits

      if digits[previous_dist-1] == 10:
       digits[previous_dist-1] = 0
       if digits[0] == 0:
        digits.insert(0,1)
     
      previous_dist -= 1

     return digits



digits = [9,9]
solution = Solution()
result = solution.plusOne(digits)

print(result)