# Power of a Number using Recursion in Python
num=int(input("Enter the number:"))
p=int(input("Enter the power:"))
def pow(num,p):
    if p != 0:
        return num * pow(num,p-1)
    else:
        return 1
print(pow(num,p))