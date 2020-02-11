'''
solution
'''
s=input()
c=0
f=len(s)
for i in range(0,len(s)):
    s1=int(s)%10
    print("your",f," in a number is :",s1)
    f=f-1
    c=c+s1
    s=int(s)/10
print("sum of your number is :",c)    
