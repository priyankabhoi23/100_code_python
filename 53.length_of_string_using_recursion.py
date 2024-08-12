def length(str):
    if str=="":
        return 0
    else:
        return 1+length(str[1:])
str="Priyanka"
print(length(str))