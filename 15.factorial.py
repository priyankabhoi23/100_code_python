num=int(input("enter the no:"))
fact=1
if num<0:
    print("not possible")

else:
    for i in range(1,num+1):
        fact=fact*i
print(fact)