class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            prod[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prod[i] *= postfix
            postfix *= nums[i]
        
        return prod
