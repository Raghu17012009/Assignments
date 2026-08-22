doll=int(input("Enter the Numbers of Dollars: "))
print("Choices")
print("1 -- Euro")
print("2 -- INR")
a=int(input("Enter your Choice: "))
if a == 1:
    curr=float(input("Enter the current rate of exchange "))
    amt=str(doll*curr)
    print("Euros = "+amt)
elif a == 2:
    curr=float(input("Enter the current rate of exchange"))
    amt=str(doll*curr)
    print("INR = "+amt)