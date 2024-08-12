# leap year or not
# using if-else
n=int(input("Enter any year:"))
if (n%400==0) or (n%4==0) and (n%100!=0):
    print("leap year")
else:
    print("not leap year")
    
# Using Calendar Module
import calendar
year=int(input("Enter the year:"))
if calendar.isleap(year):
    print("leap year")
else:
    print("not leap year")
    
# using ternary operator and function
def leap_year(y):
    return ((y%4==0) and (y%100!=0) )or (y%400==0)
y=int(input("Enter the year:"))
print(f"{y} is leap year" if leap_year(y) else f"{y} is not leap year")
