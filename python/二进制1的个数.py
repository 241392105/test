class Solution:
    def NumberOf1(self,n):
        if n<0:
            n=n & 0xffffffff
        count=0
        while n:
            count+=1
            n=(n-1) & n
        return count