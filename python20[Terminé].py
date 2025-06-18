class Solution(object):
    def maximumWealth(self, accounts):
        if len(accounts) == 0:
           return "Erreur : vide "

        somme_acc = 0

        for acc in accounts:
           if sum(acc) > somme_acc:
               somme_acc = sum(acc)
        
        return somme_acc




accounts = [[1,2,3],[3,2,1]]
solution = Solution()
result = solution.maximumWealth(accounts)
print(result)



        
        