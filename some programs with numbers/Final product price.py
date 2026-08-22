def call():
    while True:
        print("------------------------------------------------------")
        amt=(input("Enter the price of the product: "))

        if amt.lower()=="exit":
            break
        
        amt=int(amt)
        rate=float(input("Enter the tax rate: "))

        famt=amt+(amt*rate/100)

        print("Final price of the Product = "+str(famt))
    
call()
