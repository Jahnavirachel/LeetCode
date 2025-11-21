from collections import Counter
class Solution(object):
    def findErrorNums(self, nums):
        count = Counter(nums)
        for i in range(1, len(nums)+1):
            if count[i] > 1:
                d = i
            elif count[i] < 1:
                m = i
            else:
                pass
        return [d, m]
        