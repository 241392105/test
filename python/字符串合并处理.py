while True:
    try:
        a,b=raw_input().split()
        s=a+b
        t1=[]
        t2=[]
        for i in range(len(s)):
            if i%2==0:
                t1.append(s[i])
            else:
                t2.append(s[i])
        t1.sort()
        t2.sort()
        ts=[]
        for i in range(len(s)):
            if i%2==0:
                ts.append(t1.pop(0))
            else:
                ts.append(t2.pop(0))
        aTOf=['5','D','3','B','7','F']
        zeroToNine=['0','8','4','C','2','A','6','E','1','9']
        newTS=[]
        for i in ts:
            if ord(i)>96 and ord(i)<103:
                c=ord(i)-97
                newTS.append(aTOf[c])
            elif ord(i)>64 and ord(i)<71:
                c=ord(i)-65
                newTS.append(aTOf[c])
            elif ord(i)>47 and ord(i)<58:
                c=ord(i)-48
                newTS.append(zeroToNine[c])
            else:
                newTS.append(i)
        newStr=""
        for i in newTS:
            newStr+=i
        print(newStr)
    except:
        break