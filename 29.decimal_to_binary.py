num=int(input("enter decimal no:"))
binary=0
i=1
rem=0
while num !=0:
    rem=num%2
    num=num//2
    binary+=rem*i
    i*=10
print(binary)
    