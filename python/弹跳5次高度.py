def aiya(x):
    x=str(x)
    print(x)
    nr1=""
    c=0
    dot=0
    one=0
    for i in x:
        if i!='.' and c<6:
            nr1+=i
            c+=1
        elif i=='.' and c<6:
            nr1+='.'
            dot=c
        elif i!='.' and c==6:
            one=int(i)
            c+=1
    print(nr1)
    print(dot)
    print(one)
    if dot==0 and one-4>0:
        result1=int(nr1)+1
    elif dot>0 and one-4>0:
        t="0."
        for i in range(6-dot):
            if i==5-dot:
                t+='1'
            else:
                t+='0'
        result1=float(nr1)+float(t)
        print(float(nr1))
        print(float(t))
    else:
        result1=nr1
    print(result1)

a=int(input())
aiya(str(a*2.875))
aiya(str(a*0.03125))