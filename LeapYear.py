from calendar import *
year=int(input("Enter Year : "))
x=isleap(year)
if x==True:
    print(year," is leap year ")
else:
    print(year," is not a leap year ")