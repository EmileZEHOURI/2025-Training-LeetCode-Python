class Solution(object):
    def average(self, salary):
        total = float(sum(salary) - max(salary) - min(salary))/(len(salary)-2)

        return total 


   
salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
solution = Solution()
result = solution.average(salary)
print(result)
                
            
       
        