# Find the Greatest of the Two Numbers in Python Language
# using if else
n=int(input("Enter the first number:"))
m=int(input("enter the second number:"))
if n>m:
    print(n,(" is greater"))
elif n<m:
    print(m," is greater")
else:
        print(n,m," both are equal")
        
# using ternary operator
n1=int(input("Enter the firt no"))
n2=int(input("enter the secomd no"))
print(n1 if n1>n2 else n2)

# using inbuilt function max()
m1=int(input("enter the first no:"))
m2=int(input("enter the second no: "))
print(max(m1,m2))
