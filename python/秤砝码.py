n=input()
famaSize=map(int,raw_input().split())
famaNum=map(int,raw_input().split())
r=[]
for i in range(n):
    size=famaSize[i]
    t=[]
    for j in range(1,famaNum[i]+1):
        if size*j not in r:
            t.append(size*j)
    r.append(t)
print(r)