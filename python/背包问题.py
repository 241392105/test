while True:
    try:
        s,n=map(int,raw_input().split())
        a=[]
        for i in range(n):
            b=[]
            b=map(int,raw_input().split())
            a.append(b)
        b=[]
        for i in range(n):
            ts=s
            v=0
            rb=[]
            ti=i
            for t in a[i:]:
                if(t[0]<=ts and t[2]==0):
                    ts-=t[0]
                    v+=t[0]*t[1]
                    rb.append(ti)
                elif (t[0]<=ts and t[2]!=0):
                    if t[2] not in rb:
                        if (a[t[2]-1][0]+t[0]<=ts):
                            ts-=a[t[2]-1][0]+t[0]
                            v+=t[0]*t[1]+a[t[2]-1][0]*a[t[2]-1][1]
                    else:
                        ts-=a[t[2]-1][0]+t[0]
                        v+=t[0]*t[1]
                ti+=1
            b.append(v)
        print(max(b))
    except:
        break