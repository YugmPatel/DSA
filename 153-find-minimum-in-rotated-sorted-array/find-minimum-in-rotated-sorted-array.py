class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Brute Force Approach
        return min(nums)

        # Binary Search

        # result = nums[0]
        # left, right = 0, len(nums) - 1

        # while left <= right:
        #     if nums[left] < nums[right]:
        #         result = min(res, nums[left])
        #         break

        #     m = (left + right) // 2
        #     result = min(result, nums[m])
        #     if nums[m] >= nums[left]:
        #         left = m + 1
        #     else:
        #         right = m - 1
        # return result

        # Binary Search with Lower Bound

        left, right = 0, len(nums) - 1
        while left < right:
            m = left + (right - left) // 2
            if nums[m] < nums[right]:
                right = m
            else:
                left = m + 1
        return nums[left]