class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        # Backtracking
        # result = []

        # def dfs(i, curr, total):
        #     if total == target:
        #         result.append(curr.copy())
        #         return
        #     if i >= len(candidates) or total > target:
        #         return

        #     curr.append(candidates[i])
        #     dfs(i, curr, total + candidates[i])
        #     curr.pop()
        #     dfs(i + 1, curr, total)

        # dfs(0, [], 0)
        # return result
        
        # Backtracking Optimal

        result = []
        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            for j in range(i, len(candidates)):
                if total + candidates[j] > target:
                    return
                curr.append(candidates[j])
                dfs(j, curr, total + candidates[j])
                curr.pop()
        dfs(0, [], 0)
        return result