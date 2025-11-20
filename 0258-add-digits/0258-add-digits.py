class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        
        '''
        # for two digit numbers
        while num > 9:
            n = num % 10
            m = num // 10
            num = n + m
        
        return num'''

        # for any digit using mathamatical formula
        
        if num > 0:
            result = 1 + ((num - 1) % 9)
        else:
            return num
            
        return result
