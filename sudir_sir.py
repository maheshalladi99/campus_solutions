def suprout():
    try:
        z=int(input("Please enter the length of list:"))
        a=list(map(int,input().strip().split()))[:z]
    except:
        suprout()
    b=[]
    for i in range(0,len(a)):
        c=0
        for j in range(i+1,len(a)):
            if(a[j]>a[i]):
                c=c+1
            else:
                break
        b.append(c)
    print(b)
    print(max(b))
suprout()

