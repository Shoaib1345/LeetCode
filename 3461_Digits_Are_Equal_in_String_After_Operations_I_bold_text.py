class Solution(object):
    def hasSameDigits(self, s):
        digit =s[0]
        for i in s:
          if digit!=s[i]:
            return False
          else:
            return True