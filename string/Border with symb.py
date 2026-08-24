sym=input("Enter a symbol: ")
num=int(input("Enter number of times: "))

print(((sym+"  ")*(num-1)+sym+"\n")+((sym+"   "*(num-2)+"  "+sym+"\n")*num)+((sym+"  ")*(num-1)+sym+"\n"))