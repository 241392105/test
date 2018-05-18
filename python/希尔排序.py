a=map(int,raw_input().split())
step=2
c=len(a)
g=c/step
while g>0:
    for i in range(0,g):
        j=i+g
        while j<c:
            k=j-g
            while k>=0:
                if a[j]<a[k]:
                    t=a[j]
                    a[j]=a[k]
                    a[k]=t
                k-=g
            j+=g
    g/=step
print(a)