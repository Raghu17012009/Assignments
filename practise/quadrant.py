x=float(input("Enter a x coordinate: "))

y=float(input("Enter a y coordinate: "))

if x>0 and y>0:
    print("The point is in the first quadrant.")
elif x<0 and y>0:
    print("The point is in the second quadrant.")
elif x<0 and y<0:
    print("The point is in the third quadrant.")
else:
    print("The point is in the fourth quadrant.")