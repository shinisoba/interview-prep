class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxc = nums[0]
        minc = nums[0]
        maxp = nums[0]
        for i in range(1,len(nums)):
           temp = max(nums[i],nums[i]*maxc,nums[i]*minc)
           minc = min(nums[i],nums[i]*maxc, nums[i]*minc)
           maxc = temp
           maxp = max(maxc,maxp)
        return maxp
    
