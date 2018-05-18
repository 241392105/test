while True:
    try:
        a=raw_input()
        b=a.split(".")
        zero=['0','00','000','0000','00000','000000','0000000']
        if len(b)==4:
            s=""
            for i in b:
                t=bin(int(i))[2:]
                if len(t)<8:
                    c=8-len(t)-1
                    t=zero[c]+str(t)
                s+=t
            print(int(s,2))
        else:
            s=str(bin(int(a))[2:])
            if len(s)<32:
                s=zero[31-len(s)]+str(s)
            t=[s[0:8],s[8:16],s[16:24],s[24:32]]
            result=""
            for i in range(len(t)):
                if i==len(t)-1:
                    result+=str(int(t[i],2))
                else:
                    result+=str(int(t[i],2))+"."
            print(result)
    except:
        break