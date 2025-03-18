class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [0]*len(nums)
        pref = [1]*len(nums)
        suff = [1]*len(nums)
        for i in range(1,len(nums)):
            pref[i] = nums[i-1] *pref[i-1]
        for i in range(len(nums)-2,-1,-1):
            suff[i] = nums[i+1]*suff[i+1]
        for k in range(len(nums)):
            answer[k] = pref[k] * suff[k]
        return answer

  '''Input: nums = [1, 2, 3, 4]

Step 1: Initialize Arrays
answer = [0, 0, 0, 0]
pref = [1, 1, 1, 1]
suff = [1, 1, 1, 1]

Step 2: Fill pref Array
pref[1] = nums[0] * pref[0] = 1 * 1 = 1
pref[2] = nums[1] * pref[1] = 2 * 1 = 2
pref[3] = nums[2] * pref[2] = 3 * 2 = 6
Final pref = [1, 1, 2, 6]

Step 3: Fill suff Array
suff[2] = nums[3] * suff[3] = 4 * 1 = 4
suff[1] = nums[2] * suff[2] = 3 * 4 = 12
suff[0] = nums[1] * suff[1] = 2 * 12 = 24
Final suff = [24, 12, 4, 1]

Step 4: Calculate answer Array
answer[0] = pref[0] * suff[0] = 1 * 24 = 24
answer[1] = pref[1] * suff[1] = 1 * 12 = 12
answer[2] = pref[2] * suff[2] = 2 * 4 = 8
answer[3] = pref[3] * suff[3] = 6 * 1 = 6
Final answer = [24, 12, 8, 6]
'''
