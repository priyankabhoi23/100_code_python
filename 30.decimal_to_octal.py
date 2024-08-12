decimal=33
octal=0
count=1
while decimal>0:
    r=decimal%8
    octal+=r*count
    count*=10
    decimal=decimal//8
print(octal)