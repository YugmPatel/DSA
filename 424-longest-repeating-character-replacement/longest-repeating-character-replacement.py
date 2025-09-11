class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Brute Force Approach

        # result = 0
        # for i in range(len(s)):
        #     count, maxf = {}, 0
        #     for j in range(i, len(s)):
        #         count[s[j]] = 1 + count.get(s[j], 0)
        #         maxf = max(maxf, count[s[j]])
        #         if (j - i + 1) - maxf <= k:
        #             result = max(result, j - i + 1)
        # return result

        # Sliding Window

        # result = 0
        # charSet = set(s)

        # for c in charSet:
        #     count = l = 0
        #     for r in range(len(s)):
        #         if s[r] == c:
        #             count += 1

        #         while (r - l + 1) - count > k:
        #             if s[l] == c:
        #                 count -= 1
        #             l += 1
                
        #         result = max(result, r - l + 1)
        # return result

        # Slding Window with Optimal Approach

        count = {}
        result = 0

        l = 0
        maxF = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxF = max(maxF, count[s[r]])

            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            result = max(result, r - l + 1)
        return result


