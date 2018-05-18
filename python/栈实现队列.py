class Solution:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    
    def push(self,node):
        self.stackA.append(node)
    
    def pop(self):
        if not self.stackA:
            return None
        elif self.stackB:
            return self.stackB.pop()
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()

main=Solution()
main.push(5)
main.push(2)
main.push(3)
print(main.pop())    