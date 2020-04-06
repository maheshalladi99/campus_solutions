#sumofagivennu ber
while True:
    a=input()
    a=list(a)
    li=["1","2","3","4","5","6","7","8","9","0"]
    sum=0
    for i in range(0,len(li)):
        for j in range(0,len(a)):
            if li[i]==a[j]:
                sum=sum+int(li[i])
    print(sum)       
