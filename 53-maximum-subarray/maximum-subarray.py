class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # n = len(nums)
        # res = nums[0]

        # for i in range(n):
        #     cur = 0
        #     for j in range(i, n):
        #         cur += nums[j]
        #         res = max(res, cur)
        # return res


        maxSub = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub