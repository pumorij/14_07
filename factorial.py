# factorial of a number
num=int(input("Enter the number: "))
factorial=1

if(num<0):
    print("Invalid Number")
elif(num==0):
    print("Factorial is 1")
else:
    for i in range (1,num+1):
        factorial=factorial*i
    print("Factorial is ",factorial)