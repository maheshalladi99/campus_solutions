'''
a=(input()).split(" ")
b=int(a[0])
c=int(a[1])
d=(input()).split(" ")
co=0
i=0
while(True):
    if(i>len(d)-1):
        i=0
    if(len(d)==c):
        break
    d.append(int(d[i]))
    i=i+1
for i in d:
    co=co+int(i)
print(co)
print(d)'''

'''4
a 12 25
c 14 23
d 10 28
g 5  18'''

'''
a=int(input("enter number of students:"))
b=[]
d=[]
e=[]
for i in range(0,a):
    c=input().split()
    b.append(c)
print(b)
for i in range(0,a):
    d.append(int(b[i][2]))
    e.append(int(b[i][1]))
d.sort(reverse=True)
print(d,e)
for j in range(0,a):
    for k in b:
        if str(d[j]) in k:
            for l in k:
                print(l,end=" ")
                if(l==len(k)-1):
                    print("\n")
'''

a=[1,2,1,3,5]
print(set(a))
print(tuple(a))
print(dict(a))
