n1=int(input("enter the num1"))
n2=int(input("enter the num2:"))
HCF=1

for i in range(1,min(n1,n2)):
    if n1 % i==0 and n2 % i==0:
        HCF=i
print("HCF of ",n1 ,"and" ,n2, "is" ,HCF)