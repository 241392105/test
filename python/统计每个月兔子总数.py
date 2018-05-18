while True:
    try:
        a=input()
        m1=1
        m2=0
        m3=0
        for i in range(a-1):
            m3+=m2
            m2=m1
            m1=m3
        print(m1+m2+m3)
    except:
        break