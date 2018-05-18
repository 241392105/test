while True:
    try:
        a=raw_input()
        b=a.split(' ')
        r=[]
        for i in b:
            r.append(len(i))
        s=""
        ns=""
        ms=""
        for i in b:
            s+=i
        ls=[]
        for i in s:
            ls.append(i)
        x=ls[:]
        for i in x:
            if ord(i)<65 or (ord(i)>90 and ord(i)<97) or ord(i)>122:
                ns+=i
            else:
                ts=""
                rs=200
                st=0
                for it in ls:
                    if ord(it)>=97 and ord(it)<=122:
                        if ord(it)-32<rs:
                            rs=ord(it)-32
                            st=0
                    elif ord(it)>=65 and ord(it)<=90:
                        if ord(it)<rs:
                            rs=ord(it)
                            st=1
                if st==1:
                    ns+=chr(rs)
                    ls.remove(chr(rs))
                else:
                    ns+=chr(rs+32)
                    ls.remove(chr(rs+32))
        ni=0
        for i in r:
            ms+=ns[ni:i+ni]+" "
            ni+=i
        print(ms)
    except:
        break