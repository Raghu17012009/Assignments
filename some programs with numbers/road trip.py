miles=float(input("Enter the Number of Miles "))
MPG=float(input("Enter the Miles Pre Gallon "))

gas=miles/MPG

print("Gallons of Gas needed = "+str(gas))

price=float(input("Enter the Price of gas "))*gas

print("Total cost of Road trip = "+str(price))
