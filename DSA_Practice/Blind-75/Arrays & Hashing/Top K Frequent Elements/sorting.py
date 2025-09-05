class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
      count = {}
      for num in nums:
          count[num] = 1 + count.get(num, 0)

      freqArr = []
      for num, cnt in count.items():
          freqArr.append([cnt, num])
      freqArr.sort()

      result = []
      while len(result) < k:
          result.append(freqArr.pop()[1])
      return result
