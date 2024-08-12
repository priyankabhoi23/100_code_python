# using brute force algorithm
n=int(input("enter the any number"))
if n>0:
    print(n," number is positive")
elif n<0:
    print(n," number is negative")
else:
    print(n," number is zero")
    
    
# using nested if else
num1=int(input("enter the any number : "))
if num1>=0:
    if num1==0:
        print("number is zero")
    else:
        print("number is positive")
    
else:
    print("number is negative")
    
# uing ternary operator
num2=int(input("enter any number:"))
print("Positive" if num2>0  else "negative")
