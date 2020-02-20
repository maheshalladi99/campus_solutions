'''
    Arrangement of extra given spaces in the given string.
    if input is:"mahesh is a good boy        "
    output   is:"mahesh   is   a   good   boy"
    @author: Mahesh Alladi
    Created and developed on:16 Feb 2020 8:00 PM
    Duration of developing:23 Min
    
 '''


if __name__=="__main__":
    while(True):
        a=input("Give string here:")
        b=[]
        space_count=a.count(" ")
        words_count=0
        

        #it will count the number of words in a given string 
        for i in range(0,len(a)):
            if(a[i]==" " and ((i==len(a)-1) or a[i+1]==" ")):
                break
            if(a[i]==" "):
                words_count+=1
            b.append(a[i])
        words_count=words_count+1
        
        
        #displaying the actual status
        print("Your string of ",space_count,
              "spaces ",words_count,"words and len is",len(a),"\n")
        

        #nothing is there is arrange
        if words_count==1:
            print("only one word,cant arrange the sapces")
            print(a)
            print("Your string of ",space_count,
              "spaces ",words_count,"words and len is",len(a),"\n")
            

        #inserting the spaces consecutively in a defined spaces   
        space_count=space_count-(words_count-1)
        i=0
        while(True):
            if words_count==1:
                #print("only one word,cant arrange the sapces")
                break
            if space_count==0:
                break
            if(i==len(b)-1):
                i=0
                #print(space_count)
            if(b[i]==" " and b[i+1]!=" "):
                b.insert(i+1," ")
                space_count-=1
                i+=1
                #print(b)
            #space_count-=1
            i+=1
        #print(b.count(" "))
        

        #Final output of comoaring the actual and rearranged    
        if words_count>1:
            x=""
            x=x.join(b)
            #print(x,space_count,words_count)
            print("Actual one :",a,sep="")
            print("After Rearranged :",x,"\n",sep="")
            space_count1=x.count(" ")
            print("Rearranged string also, of ",space_count1,
                  "spaces ",words_count,"words and len is",len(x))
            

        #exiting of main while loop(termination)    
        exi=int(input("Press 1 to exit:"))
        if(exi==1):
            break
