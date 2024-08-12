n=int(input("Enter the no:"))
num=n
sum=0
factorial=[1]*10
for i in range(2,10):
    factorial[i]=factorial[i-1]*i
    
while n>0:
    digit=n%10
    sum+=factorial[digit]
    n=n//10
    
if sum == num:
    print(num," is a strong number")
else:
    print(num," is not a strong number")
    
    