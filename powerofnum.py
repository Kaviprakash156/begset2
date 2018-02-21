def power(K,N):
    if(N==1):
        return(K)
    if(N!=1):
        return(K*power(K,N-1))
K=int(input("Enter base: "))
N=int(input("Enter exponential value: "))
print("Result:",power(K,N))
