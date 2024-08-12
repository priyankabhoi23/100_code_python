n=int(input("enter the number:"))

print("YES" if int(str(n**2)[-len(str(n))::]) == n else "No")
