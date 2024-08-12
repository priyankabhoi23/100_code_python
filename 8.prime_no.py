# prime number or not
# Simple iterative solution
num=int(input("Enter any no:"))
flag=0
for i in range(2,num):
    if num%i==0:
        flag=1
        break

if flag==1:
    print("Not prime")
else:
    print("Prime NO")
    
# Simple iterative solution
num1=int(input("Enter any no:"))
flag=0
if num1<2:
    flag=1
else:
    for i in range(2,num):
        if num1%i==0:
            flag=1
            break

if flag==1:
    print("Not prime")
else:
    print("Prime")
    
# Optimization by n/2 iterations
num2=int(input("Enter any no"))
if num2<2:
    flag=1
else:
    for i in range(2,(int(num2/2)+1)):
        if num2%i==0:
            flag=1
            break
if flag==1:
    print("not prime")
else:
    print("Prime")
    