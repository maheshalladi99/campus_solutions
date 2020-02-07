x, y = [int(x) for x in input().split()]
z = list(map(int, input().split()))
#print(x,y,z,type(x),type(y),type(z))
co=0
su=0
i=0
while(True):
    if (co==y):
        break
    if(i>len(z)-1):
        i=0
    su=su+z[i]
    i=i+1
    co=co+1
print(su)
