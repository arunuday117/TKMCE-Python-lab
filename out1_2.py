import datetime
year=int(input("Enter the final year to which you want to display leap years : "))
tyear=datetime.datetime.now().year
for years in range(tyear,year+1):
    if years % 4 == 0 or years % 400 == 0:
        print(years," is a leap year")
    

