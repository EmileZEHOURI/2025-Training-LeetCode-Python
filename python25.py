class Solution(object):
    def lemonadeChange(self, bills):
        compte = {"5": 0, "10": 0, "20": 0}

        for bill in bills:
            if bill == 5:
                compte["5"] += 1
            elif bill == 10:
                if compte["5"] == 0:
                    return False
                compte["10"] += 1
                compte["5"] -= 1
            elif bill == 20:
                # First try to give change with one $10 and one $5
                if compte["10"] > 0 and compte["5"] > 0:
                    compte["10"] -= 1
                    compte["5"] -= 1
                # Otherwise, try to give change with three $5 bills
                elif compte["5"] >= 3:
                    compte["5"] -= 3
                else:
                    return False
        return True


bills = [5, 5, 10, 10, 20]
solution = Solution()
result = solution.lemonadeChange(bills)
print(result)  # Output should be True
