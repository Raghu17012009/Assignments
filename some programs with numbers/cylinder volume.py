
def call(n):
    n=float(n)
    if n%10!=0:
        return(n)
    else:
        n=int(n)
        return(n)

radius=call(input("Enter the radius of the cylinder: "))
height=call(input("Enter the height: "))

pi=3.14159

volume=call(pi*(radius**2)*height)

print("The volume of the cylinder is "+str(volume))
