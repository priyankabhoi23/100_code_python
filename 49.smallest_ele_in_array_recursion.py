def findmin(A,n):
    if(n==1):
        return A[0]
    return min(A[n-1],findmin(A,n-1))
if __name__== "__main__":
    
    A=[1, 4, 45, 6, -50, 10, 2]
    n=len(A)
    print(findmin(A,n))