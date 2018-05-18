while True:
    try:
        a=map(str,raw_input().split())
        s=[]
        for item in a:
            t=""
            for i in item:
                if (ord(i)>64 and ord(i)<91) or (ord(i)>96 and ord(i)<123):
                    t+=i
                else:
                    s.append(t)
                    t=""
            s.append(t)
        s.reverse()
        result=""
        for i in range(len(s)):
            if i==len(s)-1:
                result+=s[i]
            else:
                result+=s[i]+" "
        print(result)
    except:
        break