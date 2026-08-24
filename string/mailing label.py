stname=input("Enter the street name: ")
city=input("Enter the city name: ")
zipcode=int(input("Enter the zip code: "))

mailing_label=stname+",\n"+city+",\n"+str(zipcode)+"."

print("-------------------------------------\nMailing Label:")
print(mailing_label)