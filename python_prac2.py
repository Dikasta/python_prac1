def permu(a,k=0):
    #lst=[]
    if k== len(a):
        print(a)
    else:
        for i in range(k,len(a)):
            a[k],a[i] =a[i],a[k]
            permu(a,k+1)
            a[k],a[i]=a[i],a[k]


li=[1,2,3]
k=0
permu(li)
