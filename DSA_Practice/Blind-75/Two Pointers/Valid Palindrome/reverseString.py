class Solution:
    def isPalindrome(self, s: str) -> bool:
      pali = ""
      for c in s:
          if c.isalnum():
              pali += c.lower()
      return pali == pali[::-1]
