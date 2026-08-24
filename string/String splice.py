print("Enter three random words")
a=input("Enter: ")
a=a+" "
b=[]
initial=0
space=0
for i in a:
    if i==" ":
        space=a.index(i)+1
        b.append(a[initial:space-1])
        a=a[space:]

string=""
for i in range(len(b)):
    string=string+b[i]

print("www.{}.com".format(string))