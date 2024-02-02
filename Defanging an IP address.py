class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        defanged_address = address.replace(".", "[.]")
        return defanged_address

sol = Solution()
print(sol.defangIPaddr("1.1.1.1"))  
print(sol.defangIPaddr("255.100.50.0"))  
