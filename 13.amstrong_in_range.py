low=int(input("enter starting range"))
high=int(input("enter ending range"))
for n in range(low,high+1):
  
    sum=0
    temp=n
    while temp > 0:
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    if n == sum:
        print(n,",")
        
    