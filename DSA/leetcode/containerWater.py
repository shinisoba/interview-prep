class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        st = 0
        end = len(height)-1
        res = 0
        while st<end:
            area = min(height[st],height[end])*(end-st)
            res = max(area,res)
            if height[st]<height[end]:
                st+=1
            else:
                end-=1
        return res
