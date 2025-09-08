class Solution:
    def maxArea(self, height: List[int]) -> int:

        # Brute Force Approach

        # result = 0
        # for i in range(len(height)):
        #     for j in range(i + 1, len(height)):
        #         result = max(result, min(height[i], height[j]) * (j - i))
        # return result

        # Two Pointers

        left, right = 0, len(height) - 1
        result = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            result = max(result, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return result