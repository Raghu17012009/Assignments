string=input("Enter a shop name : ")

length=len(string)

side=int((20-length)/2)

length=length+(side*2)

print("="*length)

print((" "*side)+string+(" "*side))

print("="*length)