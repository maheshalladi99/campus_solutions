import math
a=input().split( )
count=0
for i in range(0,len(a)):
    root=math.sqrt(int(a[i]))
    if(int(root+0.5)**2==int(a[i])):
        count=count+1
print(count)
