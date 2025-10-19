class Solution(object):
    def isPalindrome(self, x):

        num = str(x)
        str1= num[::-1]
        return num == str1

obj = Solution()
print(obj.isPalindrome(121))
print(obj.isPalindrome(-121))
print(obj.isPalindrome("madam"))