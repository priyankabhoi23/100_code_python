# sum of digit
# Using String Character Extraction
num=input("enter any digit no:")
sumation=0
for i in num:
    sumation=sumation + int(i)
print(sumation)

# using brute force
n=int(input("Enter any no:"))
sumo=0
while n!=0:
    s=int(n%10)
    sumo=sumo+s
    n=n/10
    
print(sumo)

# Using Recursion I
num1=int(input("Enter any no:"))
sum1=0
def sumdigit(num1,sum1):
    if num1==0:
        return sum1
    digit=int(num1%10)
    sum1=sum1+digit
    return sumdigit(num1/10,sum1)
print(sumdigit(num1,sum1))
# The cool method
n1=[int(d) for d in input("Enter any no:")]
print("sum=",sum(n1))