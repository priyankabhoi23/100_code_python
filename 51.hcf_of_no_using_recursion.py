def hcf(a,b):
    if b==0:
        return b
    else:
        return(b,a%b)
num1=23
num2=69
print(hcf(num1,num2))
    