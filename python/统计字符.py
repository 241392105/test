while True:
    try:
        a=raw_input()
        b=[]
        for i in a:
            b.append(i)
        result=[0,0,0,0]
        for i in b:
            if ord(i)>47 and ord(i)<58:
                result[2]=result[2]+1
            elif ord(i)>64 and ord(i)<91 or ord(i)>96 and ord(i)<123:
                result[0]+=1
            elif i==" ":
                result[1]+=1
            else:
                result[3]+=1
        for i in result:
            print(i)
    except:
        break