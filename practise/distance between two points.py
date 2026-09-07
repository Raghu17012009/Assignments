import math
print("Enter position with space in between.")
p1=input("Enter the position of first number: ")
p2=input("Enter the position of second number: ")

x=[]
y=[]

def pos(a):
    if " " in a:
        x.append(int(a.split()[0]))
        y.append(int(a.split()[1]))

pos(p1)
pos(p2)

distance=math.sqrt((x[1]-x[0])**2+(y[1]-y[0])**2)

print(f"The distance between the two above points is: {distance}")
