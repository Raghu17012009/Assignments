def lcm(a,b):
    global gcd
    x,y=a,b
    while y:
        x,y=y,x%y
    gcd=x
    return abs(a*b)//gcd

if __name__=="__main__":
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print(f"The LCM of {a} and {b} is: {lcm(a,b)}")
    print(f"The GCD of {a} and {b} is: {gcd}")