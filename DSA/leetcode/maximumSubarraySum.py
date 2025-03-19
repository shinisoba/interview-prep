#Given an integer array nums, find the subarray with the largest sum, and return its sum.
class Solution(object):
    def maxSubArray(self, nums):
        maxs = nums[0]
        S=0
        for i in range(0,len(nums):
            s+=nums[i]
            if s>maxs:
                maxs = s
            if s<0:
                s=0
        return maxs
      
