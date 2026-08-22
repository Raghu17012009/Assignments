a=[]

def call(i):
    i+=1
    if i==1:
            b=input("Enter {} st mark: ".format(i))
            if b=="":
                call(i)
            a.append(b)
    elif i==2:
        b=input("Enter {} nd mark: ".format(i))
        if b=="":
            call(i)
        a.append(b)
    elif i==3:
        b=input("Enter {} rd mark: ".format(i))
        if b=="":
            call(i)
        a.append(b)
    

for i in range(3):
     call(i)

arr=[]

for i in range(3):
    temp=int(a[i])
    arr.append(temp)

print

sum=sum(arr)

avg=sum/3

print("The Average of three subjets is {}".format(avg))