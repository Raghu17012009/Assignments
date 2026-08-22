import math
def loop():
    def calc(num):
        box=num/6
        if num/6 == math.floor(num/6):
            box=int(num/6)
            print("Number of boxes to be bought "+str(box))
        else:
            box=math.floor(num/6)+1
            print("Number of Boxes which can be bought = "+str(box))

    num=input("Enter the Number of Cupcakes needed ")
    if num.lower()=="exit":
        return 0
    if int(num)<6:
        calc(int(num))
    else:
        calc(int(num))
    print(".......................................................")
   
    loop()
loop()