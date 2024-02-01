class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return abs(a * b) // gcd(a, b)

        
        return lcm(2, n)


solution = Solution()
print(solution.smallestEvenMultiple(5))  
print(solution.smallestEvenMultiple(6))  
