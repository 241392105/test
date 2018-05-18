while True:
    try:
        a=input()
        b=map(int,raw_input().split())
        k,d=map(int,raw_input().split())
        p=[]
        m=[]
        for i in range(len(b)):
            x=0
            xp=0
            for i in range(len(b)):
                if b[i]>x:
                    x=b[i]
                    xp=i
            m.append(x)
            p.append(xp)
            b[xp]=0
        rj=[]
        print(m)
        print(p)
        for x in range(len(p)):
            t=0
            rk=0
            j=1
            for i in range(x,len(p)):
                if i==x:
                    t=p[i]
                    j*=m[i]
                    rk+=1
                elif rk==k:
                    break
                elif t>p[i] and t-p[i]<d or p[i]>t and p[i]-t<d:
                    t=p[i]
                    j*=m[i]
                    rk+=1
            rj.append(j)
        print(max(rj))
    except:
        break