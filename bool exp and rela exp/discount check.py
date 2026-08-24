while True:

    age=input("Enter your age: ")

    if age.lower()=="exit":
        break

    age=int(age)

    boolean=bool(int(input("Are you a student (1 if true and 0 of false): ")))

    if boolean==True:
        print("You get a DISCOUNT!!!!")