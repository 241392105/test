while True:
    try:
        a=raw_input()
        if a==a[::-1]:
            print(len(a))
        else:
            maxLen=0
            for i in range(len(a)):
                if i-maxLen>=1 and a[i-maxLen-1:i+1]==a[i-maxLen-1:i+1][::-1]:
                    maxLen+=2
                    continue
                if i-maxLen>=0 and a[i-maxLen:i+1]==a[i-maxLen:i+1][::-1]:
                    maxLen+=1
            print(maxLen)
    except:
        break