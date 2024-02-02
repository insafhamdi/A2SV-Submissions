class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count_s= Counter(s)
        count_t= Counter(t)
        for i in count_t:
            if i not in count_s:
                return i
            if count_s[i]< count_t[i]:
                return i
