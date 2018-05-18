a=input()
b=[]
for i in range(a):
    t=[]
    t=map(int,raw_input().split())
    b.append(t)
for i in range(a-2,-1,-1):
    for t in range(len(b[i])):
        b[i][t]=max(b[i+1][t]+b[i][t],b[i+1][t+1]+b[i][t])
for i in b:
    print(i)