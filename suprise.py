import re

#asking for name
name=input("What is your name? ")
print("Hello, " + name + "! Welcome to the program.")

#asking about favourite colour
colour=input("What is your favourite colour? ")
print("Wow, " + colour + " is a beautiful colour! Thank you for sharing that with me, " + name + ".")

#asking about hometown
hometown=input("Where is your hometown? ")
print("Ah, " + hometown + " is a lovely place!")

#print favourite animals in the same line
print("What are your Favourite animals? ")
arr=[]
for i in range(3):
    arr.append(input("Animal "+str(i+1)+": "))
print("Your favourite animals are "+ arr[0]+","+ arr[1]+","+ arr[2]+",")  

#noun+verb+hometown
print("The  <> likes to <> in <> .")
noun=input("What is your favourite noun? ")
verb=input("What is your favourite verb? ")
print("The " + noun + " likes to " + verb + " in "+ hometown + ".")

#eg first and last name
first_name=input("What is your first name? ")
last_name=input("What is your last name? ")
print("Your full name is " + first_name + " " + last_name + ".")

a=input("Do you want a poem if so type yes or no")
if a.lower() == "yes":
    #printing a poem in multiline using escape characters
    print("Here is a short poem for you:\n")
    print("Morning drifts in soft and slow,\nA quiet breath the daylight knows.\nShadows fade where hopes begin—\nSmall sparks of light beneath the skin.")
else:
    print("No worries! Have a great day, " + name + "!")

#getting species and pet name and print it
species=input("What is the species of your pet? ")
pet_name=input("What is your pet's name? ")
print("Your " + species + "'s name is  " + pet_name + ".")

#asking the user for their line of work , the company they work for and print it
work=input("What is your line of work? ")
company=input("What company do you work for? ")
print("You are a " + work + " at " + company + ".")

#asking the usesr for a qoute and the author of the quote and print it
quote=input("What is your favourite quote? ")
author=input("Who is the author of the quote? ")
print("Quote : \"" + quote + "\" \nAuthor: " + author + ".")
