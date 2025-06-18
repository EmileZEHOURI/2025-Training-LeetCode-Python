class Solution(object):
    def calPoints(self, operations):
      
        score = []

        
        if not operations:
            return "Tableau vide"

        for op in operations:
           
            
            if op == "+":
                
                if len(score) < 2:
                    return "Erreur : Pas assez de scores précédents pour '+'."
                score.append(score[-1] + score[-2])  # 
            elif op == "D":
                
                if not score:
                    return "Erreur : Pas de score précédent pour 'D'."
                score.append(score[-1] * 2)  
            elif op == "C":
             
                if not score:
                    return "Erreur : Pas de score précédent pour 'C'."
                score.pop()  
            else:
              
                try:
                    score.append(int(op)) 
                except ValueError:
                    return "Erreur : Opération invalide."

            print(f"Score après: {score}")
        
       
        return sum(score)

tab = ["5","-2","4","C","D","9","+","+"]
solution = Solution()
result = solution.calPoints(tab)
print(f"Résultat final : {result}")
