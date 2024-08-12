# using for loop
n=int(input("enter the number:"))
sum=0
for i in range(n+1):
    sum=sum+i
print(sum)

# Using Formula for the Sum of Nth Term
num=int(input("enter the number"))
print((num*(num+1)/2))

# using recursion
def getsum(num1):
    if num1==1:
        return 1
    return num1+getsum(num1-1)
num1=int(input("enter the number"))
print(getsum(num1))

    