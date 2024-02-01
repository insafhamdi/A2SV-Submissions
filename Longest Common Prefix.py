class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:  
            return ""

        res = ""
        for i in range(len(min(strs, key=len))):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return res
            res += char
        return res 

sol = Solution()
print(sol.longestCommonPrefix(["flower", "flow", "flight"]))  
print(sol.longestCommonPrefix(["dog", "racecar", "car"]))  
