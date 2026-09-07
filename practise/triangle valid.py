sides=input("Enter the sides of triangle with space in between: ")

angles=input("Enter an angles of triangle with space in between: ")

def space(num):
    length=len(num)
    if num[length-1]==" ":
        num=num[:-1]
    return num

sides=space(sides)
angles=space(angles)

sides=[float(x) for x in sides.split()]
max_side=max(sides)

angles=[float(x) for x in angles.split()]

sides.remove(max_side)

if sum(angles)==180:
    if sum(sides)>max_side:
        print("The triangle is valid.")
    else:
        print("The triangle is not valid.")
else:
    print("The triangle is not valid.")