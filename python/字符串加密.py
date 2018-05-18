while True:
    try:
        a=raw_input()
        b=raw_input()
        na=""
        nb=""
        for i in a:
            if ord(i)>=97 and ord(i)<=121:
                na+=chr(ord(i)-31)
            elif ord(i)==122:
                na+="A"
            elif ord(i)>=65 and ord(i)<=89:
                na+=chr(ord(i)+33)
            elif ord(i)==90:
                na+="a"
            elif ord(i)>=48 and ord(i)<=56:
                na+=chr(ord(i)+1)
            elif ord(i)==57:
                na+="0"
            else:
                na+=i
        print(na)
        for i in b:
            if ord(i)>=98 and ord(i)<=122:
                nb+=chr(ord(i)-33)
            elif ord(i)==97:
                nb+="Z"
            elif ord(i)>=66 and ord(i)<=90:
                nb+=chr(ord(i)+31)
            elif ord(i)==65:
                nb+="z"
            elif ord(i)>=49 and ord(i)<=57:
                nb+=chr(ord(i)-1)
            elif ord(i)==48:
                nb+="9"
            else:
                nb+=i
        print(nb)
    except:
        break