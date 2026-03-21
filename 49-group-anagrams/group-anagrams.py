from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Brute Force Approach
        # ans = defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return list(ans.values())
        # Time: O(N*K*logK) where N is length of strs and K is maximum length of string in N. So, first loop will take O(N) and O(KlogK) because we sorted s as well

        # Space: O(N*K)


        # Optimized Approach

        anagram_dict = defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            anagram_dict[key].append(s)
        return list(anagram_dict.values())
