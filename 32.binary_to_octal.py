def convert(num):
    octal=0
    count=1
    i=0
    pos=0
    octal_array=[0]*32
    
    while num !=0:
        digit=num%10
        octal+=digit*pow(2,i)
        i+=1
        num//=10
        
        octal_array[pos]=octal
        
        if count%3==0:
            octal=0
            i=0
            pos+=1
        count+=1
        
    for j in range(pos,-1,-1):
        print(octal_array[j],end='')
binary=10101111
convert(binary)