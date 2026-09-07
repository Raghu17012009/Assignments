num=int(input("Enter a number: "))
power=int(input("Enter the power: "))
result=1
for i in range(1, power+1):
    result=result*num
    print(f"{num} raised to the power of {i} is: {result}")