class Solution(object):
    def judgeCircle(self, moves):
        h  = 0 
        v = 0
        moves = list(moves)

        for move in moves:
           if move == "U":
               h += 1
           elif move == "D":
               h -= 1
           elif move == "L":
               v -= 1
           elif move == "R":
               v += 1
           else:
            return "Erreur : La lettre n'existent pas"
                  
        coord = (h,v)

        if coord == (0,0):
             return True
        else:
             return False

        
        


tab = "LL"
solution = Solution()
result = solution.judgeCircle(tab)
print(result)