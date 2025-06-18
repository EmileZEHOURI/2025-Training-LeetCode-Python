class Solution(object):
    def canMakeArithmeticProgression(self, arr):
       arr = sorted(arr)
       ecart_type = arr[0] - arr[1] 
       for i in range(1,len(arr)-1):
        if arr[i] - arr[i+1] != ecart_type:
         return False
       return True



tab = [150,100,50,0]
solution = Solution()
result = solution.canMakeArithmeticProgression(tab)
print(result)
        