class Solution(object):
    def library(self, symbol):
     if symbol == "I": return 1
     elif symbol == "V": return 5
     elif symbol == "X": return 10
     elif symbol == "L": return 50
     elif symbol == "C": return 100
     elif symbol == "D": return 500
     elif symbol == "M": return 1000
     else :
      return 0
    
    def romanToInteger(self, s):
     a = list(s)
     numberTotal = 0

     for i in range(len(a)):

      current_value = self.library(a[i])

      if i + 1 < len(a):
       next_value = self.library(a[i+1])
       if current_value < next_value:

        numberTotal -= current_value
       else:
        numberTotal += current_value
      else:
       numberTotal += current_value
     return numberTotal

solution = Solution()
result = solution.romanToInteger("MCMXCIV")

print(result)
        
        