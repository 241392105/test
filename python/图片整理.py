while True:
    try:
        a=raw_input()
        b=[]
        for i in a:
            b.append(i)
        b.sort()
        result=""
        for i in b:
            result+=i
        print(result)
    except:
        break