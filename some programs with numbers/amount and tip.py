while True:
    amt=input("Enter the total bill Amount: ")
    if amt.lower=="exit":
        break
    if amt.isdigit!=True:
        continue
    amt=int(amt)
    tip=int(input("Enter the tip percentage: "))

    famt=amt+(amt*tip/100)    

    print("Final amount to be paid including tip is {}".format(famt))