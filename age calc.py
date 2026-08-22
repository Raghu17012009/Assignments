import datetime

date=int(input("Your bithdate : "))
print("1:Jan\n2:Feb\n3:March\n4:April\n5:May\n6:June\n7:July\n8:Aug\n9:Sept\n10:Oct\n11:Nov\n12:Dec\n")
month=int(input("Your birth month : "))
year=int(input("Your birthyear : "))

curr_time=datetime.datetime.now()

curr_date=curr_time.day
curr_month=curr_time.month
curr_year=curr_time.year

bdate=curr_date

bmonth=curr_month

byear=curr_year-year

print ("You are {} days {} months {} years old".format(bdate,bmonth,byear))
def day(date,month):
    global bmonth
    if month==2:
        date=28-date
    if month%2==0 and month!=2:
        date=30-date
    else:
        date=31-date
    return(date)

a=day(curr_date,curr_month)
a1=date

bdate=a1+a+1

bmonth= 12 - int(curr_month) + month-1

if bdate>31 or bdate>=30:
    bdate-=31
    bmonth+=1

#day(days,0)

print("Your birthday is in {} days and {} months.".format(bdate,bmonth))