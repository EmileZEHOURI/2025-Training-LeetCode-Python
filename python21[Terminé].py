import math
class Solution(object):
    def diagonalSum(self, mat):

       somme = 0
       commandGrab = False
       mid = 0

       if len(mat) == 1:
          return mat[0][0]

       if len(mat)%2 == 1:
          commandGrab = True
          middle = int(math.floor((len(mat)/2)))
          mid = mat[middle][middle]
          
       
       for i in range(len(mat)):
           for j in range(len(mat[i])):
               if i == j:
                   somme += mat[i][j]
               
       
       for i in range(len(mat)):
           for j in range(len(mat[i])):
                if j==(len(mat)-i-1):
                    somme += mat[i][j]  

       if commandGrab == True:
            somme -= mid
       
       return somme
       


mat = [[1,2,3],
       [4,5,6],
       [7,8,9]]

solution = Solution()
result = solution.diagonalSum(mat)
print("resultat", result)
