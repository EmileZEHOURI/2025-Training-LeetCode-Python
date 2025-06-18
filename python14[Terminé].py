class Solution(object):
    def lengthOfLastWord(self, s):

        s = s.split() 
        last_word = s[len(s)-1]
        return len(last_word)-1




phrase = "welcome to the jungles"
solution = Solution()
result = solution.lengthOfLastWord(phrase)
print(result)
        