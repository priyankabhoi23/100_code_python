n1=int(input("enter the no:"))
n2=int(input("enter the no:"))

for i in range(max(n1,n2),(1+(n1 * n2))):
    if i%n1==0 and i%n2==0:
        lcm=i
        break
        
print("lcm of",n1,"and ",n2, "is",lcm)