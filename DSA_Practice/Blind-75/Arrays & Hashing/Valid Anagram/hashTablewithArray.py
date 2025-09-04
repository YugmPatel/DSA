class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if len(s) != len(t):
          return False
      
      count = [0] * 26
      for i in range(len(t)):
          count[ord(s[i]) - ord('a')]+= 1
          count[ord(t[i]) - ord('a')]-= 1
      
      for j in count:
          if j != 0:
              return False
      return True
