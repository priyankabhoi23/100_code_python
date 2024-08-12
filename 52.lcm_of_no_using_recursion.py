def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a % b)
def lcm(a, b):
    return (a * b) // hcf(a, b)
num1=23
num2=69
print(lcm(num1,num2))