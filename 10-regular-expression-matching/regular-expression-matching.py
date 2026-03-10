class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def dfs(i, j):
            if j == len(p):
                return i == len(s)
            first_match = (i < len(s) and (s[i] == p[j] or p[j] == "."))
            if j + 1 < len(p) and p[j + 1] == "*":
                skip_star = dfs(i, j + 2)
                use_star = first_match and dfs(i + 1, j)
                return skip_star or use_star
            else:
                return first_match and dfs(i + 1, j + 1)
        return dfs(0, 0)