# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 14:00:15 2020

@author: admin
"""
import numpy
n=int(input("size of array:"))
l1=[]
for i in range(0,n):
    li=[]
    l1.append(li)
#print(l1)
n1=len(l1)
for i in range(0,n1):
    for j in range(0,n1):
        if(i==0 or i==n-1):
            l1[i].append("w")
for i in range(1,len(l1)-1):
    for j in range(0,len(l1)):
        l1[i].insert(j," ")
for i in range(1,n1-1):
    l1[i].insert(0,'w')
    l1[i].insert(n1-1,'w')
    l1[i].pop(n1)
    l1[i].pop(n1)
dim=int(input("demensions points:"))
for i in range(0,dim):
    row=int(input("row :"))
    col=int(input("col :"))
    l1[row][col]=1
si=int(len(l1[0])/2)

for i in range(0,len(l1[0])):
    if(i!=0 or i!=n-1):
        l1[n-1][i]='g'
l1[n-1][si]='o'
l1[n-1][0]='w'
l1[n-1][n-1]='w'
for i in l1:
    print(i)
def center(si,n,l1,comand):
    
    if (comand=='s'):
        for i in range(0,len(l1)):
            for j in range(0,len(l1[0])):
                if(l1[i][j]=='o'):
                    break
        for k in range(n-1,0,-1):
            if(l1[k][j]==1):
                l1[k][j]="X"
                break
        l1[n-1][j]='o'
        #for i in l1:
            #print(i)
        print(numpy.array(l1))
def left(si,n,l1,comand):
    if (comand=='l'):
        for i in range(0,len(l1)):
            for j in range(0,len(l1[0])):
                if(l1[i][j]=='o'):
                    l1[i][j]='g'
                    break
        for k in range(0,n):
            if(l1[i][j]=='w'):
                for l in range(0,n):
                    
                    if(l1[i][j]==1):
                        l1[i][j]="X"
                        l1[n-1][j]="o"
                        break
                    else:
                        j+=1
            else:
                i-=1
                j-=1
        #l1[n-1][j]='o'
        
        #for i in l1:
            #print(i)
        print(numpy.array(l1))
def right(si,n,l1,comand):
    if (comand=='r'):
        for i in range(0,len(l1)):
            for j in range(0,len(l1[0])):
                if(l1[i][j]=='o'):
                    l1[i][j]='g'
                    break
        for k in range(0,n):
            if(l1[i][j]=='w'):
                for l in range(0,n):
                    
                    if(l1[i][j]==1):
                        l1[i][j]="X"
                        for i in range(0,len(l1)):
                            if(l1[i][j]==1):
                                l1[i][j]="X"
                                l1[n-1][j]="o"
                                break
                            else:
                                i+=1
                        #l1[n-1][j]='o'
                        break
                    else:
                        j-=1
            else:
                j+=1
                i-=1
        #l1[n-1][j]='o'
        
        #for i in l1:
            #print(i)
        print(numpy.array(l1))
    
life=int(input("No. of lifes:"))
for i in range(0,life):
    comand=input("Give the command:")
    if(comand=='s'):
        center(si,n,l1,comand)
    if(comand=='l'):
        left(si,n,l1,comand)
    if(comand=='r'):
        right(si,n,l1,comand)
if 1 not in l1:
    print("you won the game.....")
else:
    print("you loose")
        
                        
        

