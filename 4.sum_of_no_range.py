# sum of number in given range
# using brute force (for loop)
n=int(input("Enter the starting range"))
m=int(input("Enter the ending range"))
sum=0
for i in  range(n,m+1):
    sum+=i
print(sum)

# using formula
n1=int(input("Enter the starting range"))
m2=int(input("Enter the ending range"))
sum=0
sum = int((m2*(m2+1)/2) - (n1*(n1+1)/2) + n1)
print(sum)

# using recursion
def recursum(sum,num1,num2):
    if num1>num2:
        return sum
    return num1+recursum(sum,num1+1,num2)
num1=int(input("Enter the starting range"))
num2=int(input("enter the ending range"))
sum=0
print(recursum(sum,num1,num2))
    