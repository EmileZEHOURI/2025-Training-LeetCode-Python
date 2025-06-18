class Solution(object):
    def countOdds(self, low, high):
        def count_odds_up_to(n):
            if n%2 == 0:
                return n//2
            else:
                return (n//2)+1
        return count_odds_up_to(high) - count_odds_up_to(low-1)
    


low = 800445804
high = 979430543
solution = Solution()
result = solution.countOdds(low, high)
print(result)
                
            
       
        