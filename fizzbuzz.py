class Solution:
    def fizzBuzz(self, A):
        b=[]
        for i in range(1,A+1):
            if(i%3==0 and i%5==0):
                b.append("FizzBuzz")
            elif(i%3==0):
                b.append("Fizz")
            elif(i%5==0):
                b.append("Buzz")
            else:
                b.append(str(i))
        return(b)
        # write your method here