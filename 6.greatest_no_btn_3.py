# Find the Greatest of the Three Numbers
# Using if-else Statements
n, m, p=input("Enter three no:").split()
if n>m and n>p:
    print(n," is grater")
elif m>n and m>p:
    print(m," is greater")
else:
    print(p," is greater")
    
# Using Nested if-else Statements
n1, n2, n3=input("Enter three no:").split()
if n1>=n2:
    if n1>=n3:
        print(n1," is greater")
elif n2>=n1:
    if n2>=n3:
        print(n2," is greater")
    else:
       print(n3," is greater")        

# using ternary operator
m1, m2,m3=input("Enter three no:").split()
max=m1 if m1>m2 else m2
max=m3 if m3>max else max
print(max)
