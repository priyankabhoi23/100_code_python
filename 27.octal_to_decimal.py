num=int(input("enter the octl no:"))
decimal=0
base=1
octal=num
while num:
    rem=num%10
    num=num//10
    decimal=decimal+rem*base
    base=base*8
    
print(decimal)