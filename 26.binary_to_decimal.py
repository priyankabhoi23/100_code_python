num=int(input("enter binary no:"))
binary=num
decimal=0
base=1
while num>0:
    rem=num%10
    decimal=decimal+rem*base
    num=num//10
    base=base*2
print(decimal)
    
