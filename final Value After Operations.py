class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        s = 0
        for operation in operations:
            if operation == "--X" or operation == "X--":
                s -= 1
            elif operation == "++X" or operation == "X++":
                s += 1
        return s

sol = Solution()
print(sol.finalValueAfterOperations(["--X","X++","X++"]))  
print(sol.finalValueAfterOperations(["++X","++X","X++"]))  
