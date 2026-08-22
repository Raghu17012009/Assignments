import math

a=int(input("Enter a number"))
b=int(input("Enter a number"))
op=str(input("Enter a operator"))
result=float(0.0)
def remove (a):
    if (round(a)==a):
        return (int (a))
    else:
        return a

if op=="+":
    print (a+b)
elif op=="-":
    max=max(a,b)
    min=min(a,b)
    print(max-min)
elif op=="*":
    print(a*b)
elif op=="/":
    result=a/b
    print(remove(result))