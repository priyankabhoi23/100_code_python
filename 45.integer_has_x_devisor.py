# Python program to find number of integers which has exactly x divisors
num=int(input("Enter the integer:"))
divisor=int(input("enter the devisor"))
count=0
for i in range(1,num+1):
    count_factor=0
    for j in range(1,i+1):
        if i%j==0:
            count_factor+=1
        else:
            pass
    if count_factor==divisor:
        count+=1
print(count)