class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        while num > 9:
            n = num % 10
            m = num // 10
            num = n + m
        
        return num

