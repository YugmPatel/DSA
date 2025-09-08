class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Brute Force Approach

        # result = 0
        # for i in range(len(prices)):
        #     buy = prices[i]
        #     for j in range(i + 1, len(prices)):
        #         sell  = prices[j]
        #         result = max(result, sell - buy)
        # return result

        # Two Pointers

        left, right = 0, 1
        maxP = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
        return maxP