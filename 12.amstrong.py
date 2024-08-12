num=int(input("Enter any no : "))
number=num
sum=0
tem=0
length=len(str(num))
for i in range(length):
    temp=int(num%10)
    num=num/10
    sum+=(temp*temp*temp)
print(sum)
if sum==number:
    print("Amstromg")
else:
    print("Not Amstrong")
    
