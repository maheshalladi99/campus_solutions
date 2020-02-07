l=input().split()
l1=[]
for i in range(0,len(l)):
    s=l[i]
    c=0
    for i in range(0,len(s)):
        s1=int(s)%10
        c=c+s1
        s=int(s)/10
    l1.append(c)    
print(l1)
