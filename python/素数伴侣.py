def isss(x):
    for y in range(2,x):
        if x%y==0:
            return False
    return True

while True:
    try:
        a=input()
        b=[]
        b=map(int,raw_input().split())
        s=[0 for i in range(len(b)+1)]
        c=0
        for i in range(len(b)-2,-1,-1):
            for j in range(len(b)-1,i,-1):
                if isss(b[i]+b[j]):
                    c=s[i+1]-s[j-1]+s[j+1]+1
                else:
                    c=s[i+1]
                if c>s[i]:
                    s[i]=c
        print(s[0])
    except:
        break