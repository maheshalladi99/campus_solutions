#prime number
a=int(input())
for number in range(2,a+1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number,end=" ")
