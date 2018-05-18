while True:
    try:
        a=input()
        result=[]
        for i in range(a):
            t=['0' for x in range(a-i)]
            result.append(t)
        c=1
        for x in range(a):
            for i in range(x,-1,-1):
                for j in range(0,x+1):
                    if i+j==x:
                        result[i][j]=c
                        c+=1
        for i in range(len(result)):
            for t in result[i]:
                print(str(t)+" "),
            if i<len(result)-1:
                print('\n')
    except:
        break