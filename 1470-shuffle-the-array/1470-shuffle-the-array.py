class Solution(object):
    def shuffle(self, nums, n):
        '''
        x = []
        y = []
        res = []
        x = nums[n:]
        y = nums[:n]
        for i in range(n):
            res.append(y[i])
            res.append(x[i])
        return res
        '''
        # another method
        res = []
        for i in range(n):
            res.append(nums[i])
            res.append(nums[n+i])
        return res

        
        