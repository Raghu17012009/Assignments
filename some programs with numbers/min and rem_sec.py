import re

while True:
    print("----------------------------------------------------")
    print("Enter exit to exit program")
    sec=input("Enter a large number of Seconds : ")
    if sec.lower() =="exit":
        break

    if "e" in sec and "xit" not in sec:
        print("Invalid EXIT code!!!!")
        continue
    elif sec.isdigit()!=True:
        print("Invalid Input!!!")
        continue

    sec=int(sec)

    min=sec//60

    rem_sec=sec%60

    print("{} seconds in minutes is {} and {} seconds.".format(sec,min,rem_sec))
        
