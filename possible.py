a="AABCAAADA"
k=3
while True:
    m=a[0:k]
    final_list = [] 
    for num in m: 
        if num not in final_list: 
            final_list.append(num)
    #print(final_list)
    str1 = ""     
    for ele in final_list:  
        str1 += ele      
    print(str1)
    a=a[k:len(a)]
    #print(a[k:len(a)])
    if (len(a)<1):
        break
    
