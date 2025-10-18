class Solution(object):
    def reverseVowels(self, s):
      vowel="AEIOUaeiou"
      for i in range(len(s)):
        if vowel[i] in s:
          pos=i
          print(pos)



obj =Solution()
s="IceCream"
obj.reverseVowels(s)