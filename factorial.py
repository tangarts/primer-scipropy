
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        x = 1
        for i in range(1,n+1):
            x*=i
        return x

