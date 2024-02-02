class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        lis = []
        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            lis.append(word1[i])
            lis.append(word2[j])
            i += 1
            j += 1
        while i < len(word1):
            lis.append(word1[i])
            i += 1

        while j < len(word2):
            lis.append(word2[j])
            j += 1
        return ''.join(lis)

solution = Solution()
print(solution.mergeAlternately("abc", "pqr"))  
print(solution.mergeAlternately("ab", "pqrs"))  
print(solution.mergeAlternately("abcd", "pq"))  
