a=map(int,raw_input().split())
for i in range(len(a)):
    for j in range(1,len(a)):
        if a[j]<a[j-1]:
            t=a[j]
            a[j]=a[j-1]
            a[j-1]=t
print(a)