# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result=[]
        while(matrix):
            result.append(matrix.pop(0))
            if not matrix or not matrix[0]:
                break
            matrix=self.turn(matrix)
        return result

    def turn(self,mat):
        r=len(mat)
        c=len(mat[0])
        newmat=[]
        for i in range(c):
            newmat2=[]
            for j in range(r):
                newmat2.append(mat[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat

main=Solution()
a=[]
for i in range(4):
    b=raw_input().split()
    a.append(b)
result=main.printMatrix(a)
print(result)