class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        good_pairs = 0
        for c in count.values():
            good_pairs += c * (c - 1) // 2
        
        return good_pairs

sol = Solution()

# Example 1
print(sol.numIdenticalPairs([1,2,3,1,1,3]))  

# Example 2
print(sol.numIdenticalPairs([1,1,1,1])) 

# Example 3
print(sol.numIdenticalPairs([1,2,3]))  
