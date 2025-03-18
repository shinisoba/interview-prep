#Best time to buy and sell stock

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        b = prices[0]
        S = set()
        for i in prices:
            if b>i:
                b=i
            else:
                s = i-b
                S.add(s)
        S = list(S)
        return max(S)
