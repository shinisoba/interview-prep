#finding duplicates in O(n) time
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq = {}
        result = []
        for i in nums:
            freq[i] = freq.get(i,0)+1 
        #what the previous line does is it checks if the dictionary has i in it. If it does, then it returns 1. if not, it returns 0 (as set in the bracket). 
      # we add 1 because we're adding the instance to it
        for key,value in freq.items():
            if value>1:
                result.append(key)
        return result            

"""Initial state: 
arr = [3, 3, 4, 5, 5]
freq = {}

Step 1: i = 3
freq.get(3, 0) → 0
freq[3] = 0 + 1 → 1
freq = {3: 1}

Step 2: i = 3
freq.get(3, 0) → 1
freq[3] = 1 + 1 → 2
freq = {3: 2}

Step 3: i = 4
freq.get(4, 0) → 0
freq[4] = 0 + 1 → 1
freq = {3: 2, 4: 1}

Step 4: i = 5
freq.get(5, 0) → 0
freq[5] = 0 + 1 → 1
freq = {3: 2, 4: 1, 5: 1}

Step 5: i = 5
freq.get(5, 0) → 1
freq[5] = 1 + 1 → 2
freq = {3: 2, 4: 1, 5: 2}

Final Output:
{3: 2, 4: 1, 5: 2}
"""
