a= [100,66,88,4,21,23]
for j in range(len(a)-1,0,-1):
    for i in range(j):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]
    print(a)

