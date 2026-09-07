num=int(input("Enter a number for the sum of odd numbers: "))

sum=0

for i in range(1,num+1,2):
    sum+=i

print(f"The sum of odd numbers from 1 to {num} is {sum}.")