while True:
    try:
        a=input()
        b=[]
        b=map(int,raw_input().split())
        d=[]
        m=[]
        for i in range(len(b)):
            if i==0:
                d.append(b[0])
                m.append(1)
            else:
                for t in range(len(d)-1,-1,-1):
                    if b[i]>d[len(d)-1]:
                        d.append(b[i])
                        m.append(max(m)+1)
                        break
                    elif t>0 and b[i]<=d[t] and b[i]>=d[t-1]:
                        for c in range(i-1,-1,-1):
                            if b[c]==d[t]:
                                m.append(m[c])
                                break
                        d[t]=b[i]
                        break
                    elif b[i]<=d[0]:
                        d[0]=b[i]
                        m.append(1)
                        break
        result=m
        b=b[::-1]
        m=[]
        d=[]
        for i in range(len(b)):
            if i==0:
                d.append(b[0])
                m.append(1)
            else:
                for t in range(len(d)-1,-1,-1):
                    if b[i]>d[len(d)-1]:
                        d.append(b[i])
                        m.append(max(m)+1)
                        break
                    elif t>0 and b[i]<=d[t] and b[i]>d[t-1]:
                        for c in range(i-1,-1,-1):
                            if b[c]==d[t]:
                                m.append(m[c])
                                break
                        d[t]=b[i]
                        break
                    elif b[i]<=d[0]:
                        d[0]=b[i]
                        m.append(1)
                        break
        result1=m[::-1]
        endre=[]
        # for i in m:
        #     print(i),
        for i in range(len(result)):
            endre.append(result[i]+result1[i])
        print(max(endre)+1)
    except:
        break