month=int(input("Enter the month:"))
year=int(input("Enter the year:"))
if((month==2)and ((year%4==0)or((year%100==0)and(year%400==0)))):
    print("29")
elif(month==2):
    print(28)
elif(month%2==0):
    print("30")
else:
    print("31")