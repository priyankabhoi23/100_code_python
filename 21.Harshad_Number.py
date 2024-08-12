n=int(input("Enter the number:"))
num=n
sum=0
while n>0:
    temp=n%10
    sum=sum+temp
    n=n//10
    
if num%sum==0:
    print("Harshad Number")
else:
   print("not Harshad Number")