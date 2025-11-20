class Solution(object):
    def runningSum(self, nums):
        if len(nums) > 0:
            sum_list = []
            running_list = []
            for i in range(len(nums)):
                sum_list.append(nums[i])
                num_sum = sum(sum_list)
                running_list.append(num_sum)
            return running_list
        else:
            return nums
        