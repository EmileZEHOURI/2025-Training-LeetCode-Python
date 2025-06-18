class Solution(object):

     def isPalindrome(self, x):
       a = str(x)
       tab = list(a)

       if tab == tab[::-1]:
        return True
       else:
        return False

solution = Solution()

result = solution.isPalindrome(1121)

print(result)



  
    
        