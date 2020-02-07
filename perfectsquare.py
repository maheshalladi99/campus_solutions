while 1:
    a=int(input())
    for i in range(1,int(a/2)+1):
        for j in range(1,int(a/2)+1):
            if(i==j):
                if(i*j==a):
                    c=i
                    d=j
                    a=1
                    break
    if(a==1):
        print("yes",c)
    else:
        print("no")
