# Prime Number using Recursion in Python
def prime_no(n, i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return prime_no(n,i+1)
n=int(input("enter the no:"))
if prime_no(n):
    print("yes")
else:
    print("no")