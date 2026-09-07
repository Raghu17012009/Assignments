alph=input("Enter the alphabet: ")

while len(alph)>1:
    print("Please enter a single alphabet.")
    alph=input("Enter the alphabet: ")

if alph.isalpha():
    if alph.isupper():
        print("The alphabet is in uppercase.")
    else:
        print("The alphabet is in lowercase.")
else:
    print("The input is not an alphabet.")