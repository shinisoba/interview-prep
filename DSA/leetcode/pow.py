#recursive solution 
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if x==0: 
            return 0 
        # for negative powers
        if n<0:
            return 1/(self.myPow(x,-n))
        # to cut down computation for even numbered powers
        if n%2==0:
            half = self.myPow(x,n//2)
            return half * half
        else:
            return x*self.myPow(x,n-1)
            
